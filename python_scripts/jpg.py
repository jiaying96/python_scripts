# -*- coding: UTF-8 -*-
import os
import cv2
path = 'ch4_training_images/'  #要转换的图片路径
resultPath='testResult/'       #转换后结果路径
# 获取该目录下所有文件，存入列表中
files= os.listdir(path)
for allnamejpg in files:
    img=cv2.imread(path+allnamejpg)
    cv2.imwrite(resultPath+allnamejpg,img)
    print allnamejpg+"   ok"

