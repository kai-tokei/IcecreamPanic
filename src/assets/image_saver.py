# ドット絵のキャプチャ用プログラム
# プログラムを実行してPyxel画面で Alt+1 キー を押すと
# PNG画像ファイルがデスクトップに作成される

RESOURCE = "icecream"     # リソースファイルの名前
IMAGE_NO = 0
WIDTH    = 256
HEIGHT   = 256
SCALE    = 1            # 1ドットの大きさ

import pyxel
pyxel.init(WIDTH,HEIGHT,display_scale=SCALE,capture_scale=SCALE)
pyxel.load(RESOURCE + ".pyxres")

# イメージバンク0-2を1ドット1ピクセルで保存
pyxel.image(0).save("image_0", 1)
pyxel.image(1).save("image_1", 1)
pyxel.image(2).save("image_2", 1)

pyxel.blt( 0, 0, IMAGE_NO, 0, 0, WIDTH, HEIGHT )
pyxel.show()
