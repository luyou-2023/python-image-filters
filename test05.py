#coding:utf-8
import cv2 as cv
import math
import numpy as np

#读取原始图像
img = cv.imread('images/person.jpg')

#获取图像行和列
rows, cols = img.shape[:2]

#新建目标图像
dst = np.zeros((rows, cols, 3), dtype="uint8")

#图像流年特效
for i in range(rows):
    for j in range(cols):
        #B通道的数值开平方乘以参数12
        B = math.sqrt(img[i,j][0]) * 12
        G =  img[i,j][1]
        R =  img[i,j][2]
        if B>255:
            B = 255
        dst[i,j] = np.uint8((B, G, R))

#显示图像
cv.imshow('result',np.vstack((img,dst)))
cv.waitKey()
cv.destroyAllWindows()
