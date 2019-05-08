# -*- coding: UTF-8 -*-
import os
path = 'all/'
# 获取该目录下所有文件，存入列表中
files= os.listdir(path)
n = 0.5
for allnamejpg in files:
    n += 0.5
    if(allnamejpg[-4:])=='.jpg' and allnamejpg[0:3]!='img':
        length=len(allnamejpg)
        name = allnamejpg[:-4] # #截取从头开始到倒数第四个字符之前
        oldnamejpg=path+allnamejpg
        renamejpg = path + 'img_'+str(int(n))+'.jpg'
        os.renames(oldnamejpg, renamejpg)
        print oldnamejpg+'======>'+renamejpg

        for allnametxt in files:
            if (allnametxt==name+'.txt') and allnametxt[0:2]!='gt':
                oldnametxt = path + allnametxt
                renametxt = path + 'gt_img_' + str(int(n)) + '.txt'
                os.renames(oldnametxt, renametxt)
                print oldnametxt + '======>'+renametxt
                print n