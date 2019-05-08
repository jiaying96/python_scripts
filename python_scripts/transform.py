# -*- coding: UTF-8 -*-
import os
import cv2
import numpy as np
import write_xml

filename='newlabels.txt'
xml_path='xml/'
pic_path='rename_pic/'

for line in open(filename, 'r'):
    a = line.strip().split(' ')

    c_filename=a[0]
    c_path="train_imgs\\"+c_filename+'.jpg'
    c_xmin=a[1]
    c_ymin=a[2]
    c_xmax=a[3]
    c_ymax=a[4]
    c_width=a[5]
    c_height=a[6]
    c_depth=a[7]

    write_xml.writeInfoToXml(xml_path,c_filename,c_path,c_xmin,c_ymin,c_xmax,c_ymax,c_width,c_height,c_depth)


    # num = "%05d" % counter
    # xml_name= 'img_' + num + '.xml'
    # one_xml_path = xml_path +xml_name
    # testxml.GenerateXml(a,xml_name,xml_path,xml_name)








