
# -*- coding: UTF-8 -*-

# import os
# path = 'ch4_training_images/'  #更改pic
# # 获取该目录下所有文件，存入列表中
# files= os.listdir(path)
# n = 0
# for name in files:
#     print name
#     oldname=path+name
#     print 'oldname is : ' + oldname
#     rename = path+'gt_'+name.split('.')[1] + '.jpg'
#     print 'rename is : ' + rename
#     os.renames(oldname, rename)
#     print(name, '======>', rename)



import os
path = 'ch4_training_localization_transcription_gt/'  #更改txt
# 获取该目录下所有文件，存入列表中
files= os.listdir(path)
n = 0
for name in files:
    print name
    oldname=path+name
    print 'oldname is : ' + oldname
    rename = path+'gt_'+name.split('.')[1] + '.txt'
    print 'rename is : ' + rename
    os.renames(oldname, rename)
    print(name, '======>', rename)


