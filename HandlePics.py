
#图像
import cv2 as cv
import matplotlib as plt
import numpy as np


img=cv.imread("catlina.png")
#图像显示
cv.startWindowThread() #加在这个位置
cv.imshow('image',img)
cv.waitKey(0)

img2=cv.imread("catlina.png",cv.IMREAD_GRAYSCALE) #灰度图
cv.imshow('image',img2)
cv.waitKey(0)
