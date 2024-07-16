#coding:utf-8
import cv2 as cv
import numpy as np

#读取原始图像
img = cv.imread('images/bigimage.jpg')

#图像灰度处理
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#高斯滤波降噪
gaussian = cv.GaussianBlur(gray, (5,5), 0)

#Canny算子
canny = cv.Canny(gaussian, 50, 150)

#阈值化处理
ret, result = cv.threshold(canny, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

#显示图像
#cv.imshow('src', img)
#cv.imshow('result', result)
cv.imshow('result',np.vstack((gray,result)))
cv.waitKey()
cv.destroyAllWindows()
