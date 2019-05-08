# -*- coding: utf-8 -*-
import os

import xml.etree.ElementTree as ET

import config as cf



def gen_test_data():
    test_file = open(cf.VAL_TXT_PATH, 'w')

    for img in os.listdir(cf.test_IMAGE_FOLDER):
        if 'jpg' not in img:
            continue

        # 这里改为样本图片所在文件夹的路径
        test_file.write(os.path.join(cf.test_IMAGE_FOLDER, img) + '\n')


    test_file.close()
    print('finish!')


if __name__ == '__main__':
    gen_test_data()
