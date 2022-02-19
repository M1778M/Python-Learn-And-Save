from PIL import ImageGrab
import numpy as np
import cv2 as cv
from win32api import GetSystemMetrics
import datetime
width = GetSystemMetrics(0)

heigh = GetSystemMetrics(1)
time_s = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

fcc = cv.VideoWriter_fourcc('m','p','4','v')
cap_v = cv.VideoWriter(f'output{time_s}.mp4',fcc,20.0,(width,heigh))

webcam = cv.VideoCapture(0) # Camera Number

while True:
    img = ImageGrab.grab(bbox=(0,0,width,heigh))
    img_np = np.array(img)
    img_final = cv.cvtColor(img_np,cv.COLOR_BGR2RGB)
    _,frame = webcam.read()
    fr_h ,fr_w,_ = frame.shape
    img_final[0:fr_h,0:fr_w,:] = frame[0:fr_h,0:fr_w,:]
    #cv.imshow('webcam',frame)
    cv.imshow('Title',img_final)
    cap_v.write(img_final)
    if cv.waitKey(10) == ord('q'):
        break
    