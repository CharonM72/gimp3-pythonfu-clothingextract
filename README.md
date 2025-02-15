# gimp3-pythonfu-clothingextract
A fairly simple GIMP 3.0 Python-fu script that will export the full, flattened, current image as a .png with smart filenaming.

This Python-Fu script for GIMP 3.0 automates the process of extracting clothing from an image. It is designed for use with two aligned images: one of a person wearing clothing and another of the same person wearing only underwear (or no clothing). The script isolates the clothing by calculating the difference between the two images, creating a mask, and applying it to the clothed layer. The result is a layer with the clothing extracted and a transparent background, ready for use in creating "dressable" characters or layered clothing designs.

## Key Features:
- Automated Workflow: Streamlines the process of isolating clothing from images.

- Transparency Support: Creates a transparent background for the extracted clothing.

- GIMP 3.0 Compatibility: Built for GIMP 3.0 using Python 3 and the updated GIMP API.

## Use Cases:
- Creating dressable characters for games or animations.

- Designing layered clothing for digital art or fashion projects.

- Isolating clothing elements for photo editing or compositing.

## Requirements:
- GIMP 3.0 or later.

- Two aligned images: one clothed and one unclothed.

## How to Use:
1. Place the extract_clothing.py file (or clone the repo) into:  
**Windows:**
C:\Users\[yourname]\AppData\Roaming\GIMP\3.0\plug-ins\extract_clothing  
**Unix-like:**
~/.config/GIMP/3.0/plug-ins/extract_clothing/

2. In GIMP 3.x, load the clothed image as the top layer and the unclothed image as the bottom layer.

3. Run the script via Filters > Clothing > Extract Clothing. Give it a few seconds to finish.

4. The clothed layer will now have a transparent background where the clothing was extracted.