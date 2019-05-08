# -*- coding:UTF-8 -*-
import requests
import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 定义下载函数
def download(url, filename):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)

# 创建下载目录
if os.path.exists('imgs') is False:
    os.makedirs('imgs')




browser = webdriver.Chrome()
# 打开谷歌浏览器Chrome
url = 'https://www.geetest.com/Sensebot/'
browser.get(url)
time.sleep(1)
# 点击  点击按钮进行验证
play = browser.find_element_by_xpath("//*[@id='captcha']/div[3]/div[2]/div[1]/div[3] ").click()
time.sleep(5)


while True:
    for j in range(0,6):
        #定位到图片
        # img = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/img")
        img = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/img")
        #定位到图片链接
        target_url = img.get_attribute("src")
        print("target_url    " + target_url)
        #图片名称
        img_name = target_url.split('/')[-1].split('?')[0]
        filename = os.path.join('imgs', img_name)
        print("filename    " + filename)
        #下载文件
        download(target_url, filename)
        print('%d/6'%j)
        #点击刷新
        refresh = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/div/div[3]/div/a[2]").click()
        time.sleep(3)
    # 点击 尝试次数过多，请重新尝试  //*[@id="captcha"]/div[3]/div[2]/div[1]/div[3]/span[2]
    # element   <span class="geetest_reset_tip_content">请点击重试</span>
    reset = browser.find_element_by_xpath("//*[@id='captcha']/div[3]/div[2]/div[1]/div[3]/span[2]").click()
    time.sleep(3)
# 关闭浏览器
browser.quit()







