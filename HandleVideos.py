import cv2 as cv
import matplotlib as plt
import numpy as np

#cv2.VideoCapture可以捕获摄像头用数字来控制不同的设备
vc=cv.VideoCapture('cvTest.MP4')
#检查是否打开正确
if vc.isOpened():
    open,frame=vc.read()#返回第一个参数oepn是bool类型(标记是否打开)，第二个人参数表示这一帧
else:
    open=False

#遍历每一帧
while open:
    flag,frame=vc.read()
    if frame is None:
        break
    if flag==True:
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('result',gray)
        if cv.waitKey(10)&0xFF==27: #每次处理完一帧等待100ms & 播放途中按了退出键
            break
vc.release()
cv.destroyAllWindows()

