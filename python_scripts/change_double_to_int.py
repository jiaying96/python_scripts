# -*- coding:UTF-8 -*-
import os
path = 'gt/'  #要转换的txt路径
resultPath='new_gt/'       #转换后txt路径
# 获取该目录下所有文件，存入列表中
files= os.listdir(path)
for filename in files:
    print (filename)
    f = open(path+filename, "r+", encoding='UTF-8')
    while True:
        line = f.readline()
        if line:
            pass  # do something here
            line = line.strip()
            # print (line)
            x1, y1, x2, y2, x3, y3, x4, y4, content = line.split(',', 8)
            line = str(int(float(x1))) + ',' + str(int(float(y1))) + ',' + str(int(float(x2))) + ',' + str(
                int(float(y2))) + ',' + str(int(float(x3))) + ',' + str(int(float(y3))) + ',' + str(
                int(float(x4))) + ',' + str(int(float(y4))) + ',' + "###"
            # print (line)
            with open(resultPath+filename, 'a+', encoding='UTF-8') as l:
                l.write(line + '\n')
            # f.write(line)

        else:
            break
    print ("ok")
    f.close()





