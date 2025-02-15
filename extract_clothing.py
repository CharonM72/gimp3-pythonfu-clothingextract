#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Clothing Extraction Script for GIMP 3.0
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gimp', '3.0')
gi.require_version('GimpUi', '3.0')
gi.require_version('Gegl', '0.4')
from gi.repository import Gimp, GimpUi, GObject, GLib, Gegl

def N_(message): return message
def _(message): return GLib.dgettext(None, message)

class ClothingExtractPlugin(Gimp.PlugIn):
    ## Plugin Setup ##
    def do_set_i18n(self, procname):
        return False
    
    def do_query_procedures(self):
        return ["clothing-extract"]
    
    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.run, None)
        procedure.set_image_types("*")
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.DRAWABLE)
        procedure.set_menu_label(_("Extract Clothing"))
        procedure.add_menu_path('<Image>/Filters/')
        
        procedure.set_documentation(
            _("Extract Clothing"),
            _("Extract clothing from a clothed image using an unclothed reference"),
            name
        )
        procedure.set_attribution("Charon", "GPL 3", "2025")
        return procedure

    ## Main Logic ##
    def run(self, procedure, run_mode, image, drawable, args, data):
        try:
            # Start undo group
            image.undo_group_start()

            # Get layers (clothed should be top layer)
            layers = image.get_layers()
            if len(layers) < 2:
                raise ValueError("Need exactly 2 layers (clothed top, unclothed bottom)")
            
            clothed_layer = layers[0]

            # Set Difference mode
            clothed_layer.set_mode(Gimp.LayerMode.DIFFERENCE)

            # Create white mask
            mask = clothed_layer.create_mask(Gimp.AddMaskType.WHITE)
            clothed_layer.add_mask(mask)

            # Create visible composite layer
            visible_layer = Gimp.Layer.new_from_visible(image, image, "Threshold Base")
            image.insert_layer(visible_layer, None, -1)  # Insert at the bottom

            # Apply threshold
            threshold_proc = Gimp.get_pdb().lookup_procedure("gimp-drawable-threshold")
            config = threshold_proc.create_config()
            config.set_property("drawable", visible_layer)
            config.set_property("channel", Gimp.HistogramChannel.VALUE)
            config.set_property("low-threshold", 0.03)  # Adjust as needed
            config.set_property("high-threshold", 1.0)
            threshold_proc.run(config)

            # Copy visible and paste into mask
            Gimp.edit_copy_visible(image)
            paste_result = Gimp.edit_paste(mask, True)

            if paste_result and len(paste_result) > 0:
                floating_sel = paste_result[0]
                if floating_sel.is_floating_sel():
                    # Anchor the floating selection
                    anchor_proc = Gimp.get_pdb().lookup_procedure("gimp-floating-sel-anchor")
                    config = anchor_proc.create_config()
                    config.set_property("floating-sel", floating_sel)
                    anchor_proc.run(config)
                else:
                    raise RuntimeError("Paste result is not a valid floating selection")
            else:
                raise RuntimeError("Failed to paste into mask")

            # Cleanup
            image.remove_layer(visible_layer)
            clothed_layer.set_mode(Gimp.LayerMode.NORMAL)

            # Apply the mask (merge it with the layer)
            remove_mask_proc = Gimp.get_pdb().lookup_procedure("gimp-layer-remove-mask")
            config = remove_mask_proc.create_config()
            config.set_property("layer", clothed_layer)
            config.set_property("mode", Gimp.MaskApplyMode.APPLY)
            remove_mask_proc.run(config)

            # Update the display
            Gimp.displays_flush()
            image.undo_group_end()
            return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

        except Exception as e:
            image.undo_group_end()
            error = GLib.Error.new_literal(Gimp.PDBStatusType.EXECUTION_ERROR, str(e))
            return procedure.new_return_values(Gimp.PDBStatusType.EXECUTION_ERROR, error)

Gimp.main(ClothingExtractPlugin.__gtype__, sys.argv)