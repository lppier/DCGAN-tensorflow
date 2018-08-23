import os
import cv2

src = "C:/Users/pierl/PycharmProjects/DCGAN-tensorflow/data/monocyte"
dst = "C:/Users/pierl/PycharmProjects/DCGAN-tensorflow/data/monocyte_resized"

os.mkdir(dst)

for each in os.listdir(src):
    img = cv2.imread(os.path.join(src, each))
    img = cv2.resize(img, (128, 128))
    cv2.imwrite(os.path.join(dst, each), img)