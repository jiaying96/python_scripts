# -*- coding: UTF-8 -*-
import os
import re


import cv2
def txt():
    path='results/'
    i=1
    txt = open(path+'comp4_det_test_2.txt', "r").read()
    for line in open(path+'comp4_det_test_2.txt','r'):
        a = line.split(' ')
        picname = a[0]  #文件名
        #print(picname)
        count=len(re.findall(picname, txt))
        #print(count)
        xmin=int(float(a[2]))
        ymin=int(float(a[3]))
        xmax=int(float(a[4]))
        ymax=int(float(a[5]))
        img = cv2.imread("test_imgs/" + picname + '.jpg')
        #print(img.shape)
        cropped = img[ymin:ymax, xmin:xmax]  # 裁剪坐标为[y0:y1, x0:x1]
        newname=picname +'_'+ str(i) + ".jpg"
        print(newname)
        cv2.imwrite(path + newname, cropped)
        if(i<count):
            i+=1
        else:
            i=1
txt()