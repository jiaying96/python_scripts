import os
path = 'res/'  #这里写的是相对路径，也可以写绝对路径
# 获取该目录下所有文件，存入列表中
f = os.listdir(path)
n = 0
for i in f:
    #print("Current directory is: %s" % os.getcwd()) 查看当前路径
    #原文件名
    oldname =path+'gt_img_' + str(n + 1) + '.txt'
    # 设置新文件名
    newname = path+'res_img_' + str(n + 1) + '.txt'
    # 用os模块中的rename方法对文件改名
    os.renames(oldname, newname)
    print(oldname, '======>', newname)
    n += 1
