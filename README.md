# gimp3-pythonfu-clothingextract
# English
A fairly simple GIMP 3.0 Python-fu script that will export the full, flattened, current image as a .png with smart filenaming.

This Python-Fu script for GIMP 3.0 automates the process of extracting clothing from an image. It is designed for use with two aligned images: one of a person wearing clothing and another of the same person wearing only underwear (or no clothing). The script isolates the clothing by calculating the difference between the two images, creating a mask, and applying it to the clothed layer. The result is a layer with the clothing extracted and a transparent background, ready for use in creating "dressable" characters or layered clothing designs.

(Possibly the major use case for this is for working with "difference" images by artists, known in the Japanese dōjin art community as 差分)

### Key Features
- Automated Workflow: Streamlines the process of isolating clothing from images.

- Transparency Support: Creates a transparent background for the extracted clothing.

- GIMP 3.0 Compatibility: Built for GIMP 3.0 using Python 3 and the updated GIMP API.

### Use Cases
- Creating dressable characters for games or animations.

- Designing layered clothing for digital art or fashion projects.

- Isolating clothing elements for photo editing or compositing.

### Requirements
- GIMP 3.0 or later.

- Two aligned images: one clothed and one unclothed. Note that the images must be essentially identical except for the clothing, or there may be unexpected results.

### Limitations
- The script extracts anything visibly different from the two images, to an almost pixel-perfect degree, so if the images are for instance, slightly misaligned, or have different compression artifacts, or different color tones etc. then it may pull large amounts of the original image with the clothing and essentially fail.

- It will also extract things such as clothing shadows that may not exist on the unclothed image, or alterations in the skin due to the clothing. If the facial expression differs, then that will also be extracted. Keep in mind all of this can be manually cleaned up with the eraser tool as needed.

### How to Use
1. Place the extract_clothing.py file (or clone the repo) into:  
**Windows:**  
C:\Users\[yourname]\AppData\Roaming\GIMP\3.0\plug-ins\extract_clothing  
**Unix-like:**  
~/.config/GIMP/3.0/plug-ins/extract_clothing/

2. In GIMP 3.x, load the clothed image as the top layer and the unclothed image as the bottom layer.

3. Run the script via Filters > Extract Clothing. Give it a few seconds to finish.

4. The clothed layer will now have a transparent background where the clothing was extracted.

- The script can handle multiple clothed images at once - just hide any images that you don't want to be considered.
    - For instance, let's say layer 1 is wearing a jacket and undershirt, layer 2 is wearing only an undershirt, and layer 3 is wearing no shirt, and thus the layers are ordered from most to least clothed:
        - If you want to extract *just* the jacket, then leave all layers visible. The script will compare the jacket/undershirt image against the undershirt, thus extracting only the jacket.
        - If you want to extract the jacket *and* the undershirt as a single layer, then hide the undershirt layer. The script will compare the jacket/undershirt image against the shirtless image, thus extracting both the jacket and the undershirt.
        - If you want to extract the *just* the undershirt, then hide the jacket/undershirt layer. The script will compare the undershirt image against the shirtless image, thus extracting just the undershirt, and the jacket image will be untouched.
    - This also works if you have a bunch of unrelated clothing layers over a bottom unclothed layer. Simply hide all layers except the unclothed one and the layer whose clothing you wish to extract, and run the script.

## 日本語
gimp3-pythonfu-clothingextract
GIMP 3.0用のPython-fuスクリプトで、現在の画像をフラット化してスマートなファイル名で.pngとしてエクスポートします。

このPython-Fuスクリプトは、画像から衣装を抽出するプロセスを自動化します。衣装を着た人物の画像と、下着のみ（または何も着ていない）の同じ人物の画像を使用するように設計されています。スクリプトは、2つの画像の差分を計算し、マスクを作成して衣装レイヤーに適用することで、衣装を分離します。結果として、衣装が抽出され、透明な背景を持つレイヤーが作成されます。これにより、「着せ替え」キャラクターやレイヤード衣装デザインの作成に使用できます。

（このスクリプトの主な使用例は、日本の同人アートコミュニティで「差分」として知られる画像を扱うことです。）

### 主な機能
- 自動化されたワークフロー: 画像から衣装を分離するプロセスを効率化します。

- 透明背景のサポート: 抽出された衣装に透明な背景を作成します。

- GIMP 3.0対応: Python 3と更新されたGIMP APIを使用してGIMP 3.0向けに構築されています。

### 使用例
- ゲームやアニメーション用の着せ替えキャラクターの作成。

- デジタルアートやファッションデザインプロジェクトのためのレイヤード衣装のデザイン。

- 写真編集や合成のための衣装要素の分離。

### 必要な環境
- GIMP 3.0以降。

- 2つの整列された画像: 1つは衣装を着た画像、もう1つは衣装を着ていない画像。画像は衣装以外の部分がほぼ同一である必要があります。そうでない場合、予期しない結果が生じる可能性があります。

### 制限事項
- スクリプトは、2つの画像の視覚的な差分をほぼピクセル単位で抽出するため、画像が少しでもずれていたり、圧縮のアーティファクトが異なっていたり、色調が異なっていたりすると、衣装と一緒に元の画像の大部分が抽出され、失敗する可能性があります。

- 衣装の影や、衣装による肌の変化なども抽出されます。また、表情が異なる場合、その部分も抽出されます。これらは必要に応じて消しゴムツールで手動で修正できます。

### 使用方法
1. extract_clothing.pyファイルを以下のディレクトリに配置します（またはリポジトリをクローンします）:  
**Windows:**  
C:\Users\[ユーザーネーム]\AppData\Roaming\GIMP\3.0\plug-ins\extract_clothing  
**Unix系:**  
~/.config/GIMP/3.0/plug-ins/extract_clothing/

2. GIMP 3.xで、衣装を着た画像を最上位レイヤーとして、衣装を着ていない画像を下位レイヤーとして読み込みます。

3. フィルター > Extract Clothingを抽出からスクリプトを実行します。完了するまで数秒待ちます。

4. 衣装レイヤーには、衣装が抽出された部分が透明な背景になります。

- このスクリプトは、複数の衣装画像を一度に処理できます。不要な画像は非表示にしてください。
    - 例えば、レイヤー1がジャケットと下着を着ており、レイヤー2が下着のみを着ており、レイヤー3が何も着ていない場合、レイヤーは最も着ているものから順に並べます：
        - ジャケットのみを抽出したい場合：すべてのレイヤーを表示したままにします。スクリプトは、ジャケット/下着の画像を下着の画像と比較し、ジャケットのみを抽出します。
        - ジャケットと下着を1つのレイヤーとして抽出したい場合：下着のレイヤーを非表示にします。スクリプトは、ジャケット/下着の画像をシャツを着ていない画像と比較し、ジャケットと下着の両方を抽出します。
        - 下着のみを抽出したい場合：ジャケット/下着のレイヤーを非表示にします。スクリプトは、下着の画像をシャツを着ていない画像と比較し、下着のみを抽出します。ジャケットの画像はそのまま残ります。
    - これは、一番下に「着ていない」レイヤーがあり、その上に無関係な衣装レイヤーが複数ある場合にも適用されます。抽出したい衣装のレイヤーと「着ていない」レイヤー以外をすべて非表示にして、スクリプトを実行してください。