# -*- coding: UTF-8 -*-
import os

def txt():
	path='yanzheng/'
	for line in open('labels.txt','r'):
		a = line.split(':')
		picname = a[0]  #文件名
		context = a[1]  #四个坐标信息
		dir2 = path + "\\" + picname.split('.')[0]+ '.txt'
		f = open(dir2, 'a+')
		f.write('%s' %context)
	print("txt ok")

def renameall():
	path_all = 'yanzheng/'
	# 获取该目录下所有文件，存入列表中
	files= os.listdir(path_all)
	n = 0.5
	for allnamejpg in files:
		n += 0.5
		if(allnamejpg[-4:])=='.jpg':
			length=len(allnamejpg)
			name = allnamejpg[:-4]
			oldnamejpg=path_all+allnamejpg
			renamejpg = path_all + 'img_'+str(int(n))+'.jpg'
			os.renames(oldnamejpg, renamejpg)
			print oldnamejpg+'======>'+renamejpg

			for allnametxt in files:
				if (allnametxt==name+'.txt'):
					oldnametxt = path_all + allnametxt
					renametxt = path_all + 'gt_img_' + str(int(n)) + '.txt'
					os.renames(oldnametxt, renametxt)
					print oldnametxt + '======>'+renametxt
	print("rename ok")

txt()
renameall()






