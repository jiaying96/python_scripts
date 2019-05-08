# -*- coding: UTF-8 -*-
import os
import cv2
import numpy as np

new_label_path='newlabels.txt'
label_path='labels.txt'
path_all = 'crop/'
result_path = 'result_pic/'
rename_pic_path='rename_pic/'
txt_count = len(open(label_path, 'r').readlines())

breaknum=1237

counter=breaknum

width = 0
height = 0
depth = 0


for line in open(label_path, 'r'):
    a = line.split(' ')
    txtpicname = a[0].split('/')[1]
    with open('log.txt', 'a+',encoding="utf-8") as l:  #encoding="utf-8"是因为带中文
        l.write("###########################################\n")
        l.write(txtpicname+'\n')

    num = "%05d" % counter
    new_pic_name= 'img_' + num


    

    # 获取该目录下所有文件，存入列表中
    files = os.listdir(path_all)
    for picname in files:
        if (picname == txtpicname):
            file_path=path_all+picname
            # Python读取中文命名的图片
            img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
            # cv2.imshow('img',img)
            # cv2.waitKey(0)
            new_file_path=result_path+picname
            # Python保存中文命名的图片
            cv2.imencode('.jpg', img)[1].tofile(new_file_path)
            with open('log.txt', 'a+',encoding="utf-8") as l:
                l.write(picname + '\n')
                l.write("###########################################\n")

            imr_result_path=result_path+picname
            # Python读取中文命名的图片
            img_result = cv2.imdecode(np.fromfile(imr_result_path, dtype=np.uint8), -1)
            new_file_path = rename_pic_path + new_pic_name + '.jpg'
            # Python保存中文命名的图片
            cv2.imencode('.jpg', img_result)[1].tofile(new_file_path)

            #读取已经重命名的图片
            img3=cv2.imread(new_file_path)
            height=img3.shape[0]
            width = img3.shape[1]
            depth=img3.shape[2]

    with open(new_label_path, 'a+') as l:
        l.write('%s %s %s %s %s %d %d %d \n' % (new_pic_name, (a[1]), a[2], a[3], a[4],width,height,depth))

    if counter<=txt_count+breaknum:
        counter+=1






