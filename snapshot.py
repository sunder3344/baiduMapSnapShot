'''
Created on 2020年4月15日

@author: Sunder
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

class SnapShot(object):
    url = ""
    def __init__(self):
        pass
        
    def searchAddr(self, address, screenHeight, screenWidth, runBack = True):
        chromeopt = Options()
        if runBack == True:
            chromeopt.add_argument('--headless')
            chromeopt.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chromeopt)
        driver.get('http://map.baidu.com')
        driver.implicitly_wait(5)
        time.sleep(2)
        #将屏幕分辨率放大很多
        driver.set_window_size(screenHeight, screenWidth, 'current')
        #搜索地址
        word = driver.find_element_by_class_name("searchbox-content-common")
        word.send_keys(address)
        button = driver.find_element_by_id("search-button")
        button.click()
        time.sleep(5)
        #屏幕最大化
        driver.maximize_window()
        time.sleep(1)
        #隐藏前先放大至最高比例尺
        zoomIn = driver.find_element_by_class_name("BMap_stdMpZoomIn")
        zoomIn.click()
        time.sleep(1)
        zoomIn.click()
        time.sleep(1)
        
        #按F11
#         k = PyKeyboard()
#         k.press_key(k.function_keys[11])
        #隐藏搜索框
        panel = driver.find_element_by_id("left-panel")
        driver.execute_script("return arguments[0].style='display:none;'", panel)
        #隐藏迁徙大数据图标
        icon = driver.find_element_by_id("ui3_springfestival_data")
        driver.execute_script("return arguments[0].style='display:none;'", icon)
        #隐藏工具栏
        tool = driver.find_element_by_id("app-right-top")
        driver.execute_script("return arguments[0].style='display:none;'", tool)
        #隐藏指南针
        compass = driver.find_element_by_id("map-operate")
        driver.execute_script("return arguments[0].style='display:none;'", compass)
        #隐藏wrapper
        wrapper = driver.find_element_by_id("mapType-wrapper")
        driver.execute_script("return arguments[0].style='display:none;'", wrapper)
        #隐藏logo
        logo = driver.find_element_by_id("newuilogo")
        driver.execute_script("return arguments[0].style='display:none;'", logo)
        #隐藏logo
        desc = driver.find_element_by_class_name("BMap_cpyCtrl")
        driver.execute_script("return arguments[0].style='display:none;'", desc)
        pos = driver.get_window_position()
#         print(pos)
        width = driver.execute_script("return document.body.parentNode.scrollWidth")
        height = driver.execute_script("return document.body.parentNode.scrollHeight")
#         print(width)
#         print(height)
#         ActionChains(driver).move_by_offset(width/2, height/2).perform()
#         ActionChains(driver).double_click(None).perform()
#         ActionChains(driver).double_click(None).perform()
#         ActionChains(driver).double_click(None).perform()
#         ActionChains(driver).double_click(None).perform()
#         ActionChains(driver).double_click(None).perform()
        time.sleep(3)
#         m = PyMouse()
#         m.move(width, 50)
#         time.sleep(3)
#         driver.save_screenshot("./1.png")
#         m.drag(0, 50)
        print("wait")
        driver.save_screenshot("./1.png")
        
if __name__ == '__main__':
    snap = SnapShot()
    #此处分辨率8000*8000估计耗时10分钟左右
    snap.searchAddr("宜山路757号", 8000, 8000, False)
    time.sleep(10)
    print("Success!")