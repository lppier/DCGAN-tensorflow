import os
import cv2

src = "./data/lymphocyte"
dst = "./data/lymphocyte_resized"

os.mkdir(dst)

for each in os.listdir(src):
    img = cv2.imread(os.path.join(src, each))
    img = cv2.resize(img, (64, 64))
    cv2.imwrite(os.path.join(dst, each), img)