#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2018/12/22 15:37
@Author  : Negen
@Site    : 
@File    : downLoadProject.py
@Software: PyCharm
'''
import time

from selenium import webdriver
import re
import requests


def getValidateCode(NET_SessionId):
    baseUrl = 'http://218.6.132.58/'
    request = requests.session()
    headers = {
        "Host": "218.6.132.58",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://218.6.132.58/",
        "Connection": "keep-alive",
        "Cookie": "username=201410803007; ASP.NET_SessionId=" + NET_SessionId
    }

    validateCodeUrl = 'http://218.6.132.58/ValidCode.ashx?d=1545442068502'
    respValidate = request.get(validateCodeUrl, headers=headers)
    validateCode = respValidate.text
    return validateCode

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:/毕设'}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)




baseUrl = 'http://218.6.132.58'
driver.get(baseUrl)
cookies = driver.get_cookies()
NET_SessionId = cookies[0]['value']
validateCode = getValidateCode(NET_SessionId)

# validateCodeUrl = 'http://218.6.132.58/ValidCode.ashx?d=1545442068502'
# driver.get(validateCodeUrl)
# validateCode = re.findall("<body>(.*?)</body>", driver.page_source, re.S)[0]

driver.find_element_by_id('txtUserId-inputEl').send_keys("***********")     #账号
driver.find_element_by_id('txtPassword-inputEl').send_keys("****")           #密码
driver.find_element_by_id('txtValid-inputEl').send_keys(validateCode)         #验证码
driver.find_element_by_id('comboGrade-inputEl').send_keys("2014")            #年纪
driver.find_element_by_id('btnSubmit-btnEl').click()

time.sleep(2)
downLoadFileUrl = 'http://218.6.132.58/AchievementUpload.aspx?url=AchievementUpload.aspx&_dc=1545467288338&'
driver.get(downLoadFileUrl)

time.sleep(2)
driver.find_element_by_id('button-1023-btnIconEl').click()



