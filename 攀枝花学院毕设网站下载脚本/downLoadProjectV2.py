#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2018/12/22 15:37
@Author  : Negen
@Site    : 
@File    : downLoadProject.py
@Software: PyCharm
'''
import codecs
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse
import re
import requests



def login(username, password):
    baseUrl = 'http://218.6.132.58/'
    request = requests.session()
    resp = request.get(baseUrl)
    html = BeautifulSoup(resp.text, 'lxml')
    NET_SessionId = resp.cookies['ASP.NET_SessionId']
    __EVENTVALIDATION = html.find('input', {'id': '__EVENTVALIDATION'})['value']
    __VIEWSTATE = html.find('input', {'id': '__VIEWSTATE'})['value']

    # print(request.cookies)
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

    # 验证码地址
    # validateImageUrl = 'http://218.6.132.58/ImageCode.aspx?d=1545442068502'
    # request.get(validateImageUrl)
    validateCodeUrl = 'http://218.6.132.58/ValidCode.ashx?d=1545442068502'
    respValidate = request.get(validateCodeUrl, headers=headers)
    validateCode = respValidate.text
    # print(respValidate.text)

    # 登陆表单数据
    postData = {
        "submitDirectEventConfig": {"config": {"extraParams": {"gradId": "100000128"}}},
        "__EVENTTARGET": "ResourceManager1",
        "__EVENTARGUMENT": "btnSubmit|event|Click",
        "__VIEWSTATE": __VIEWSTATE,
        "__EVENTVALIDATION": __EVENTVALIDATION,
        "txtUserId": username,
        "txtPassword": password,
        "txtValid": validateCode,
        "comboGrade": "2014",
        "_comboGrade_state": [{"value": "100000128", "text": "2014", "index": 0}]
    }

    postHeaders = {
        "Host": "218.6.132.58",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Accept": "*/*",
        "X-Ext.Net": "delta=true",
        "Origin": "http://218.6.132.58",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://218.6.132.58/",
        "Connection": "keep-alive",
        "Cookie": "username=201410803007; ASP.NET_SessionId=" + NET_SessionId
    }

    loginUrl = 'http://218.6.132.58/'
    postData = parse.urlencode(postData)
    loginResult = request.post(loginUrl, headers=postHeaders, data=postData)

    # print(loginResult.text)
    mainPageUrl = 'http://218.6.132.58/layout.aspx?t=1545442068502'
    mainPageResp = request.get(mainPageUrl, headers=headers)

    """
    登陆失败数据
    <script>window.parent.parent.self.location.href='http://218.6.132.58';</script>
    """
    failStr = "<script>window.parent.parent.self.location.href='http://218.6.132.58';</script>"
    if mainPageResp.text == failStr:
        #print("登陆失败")
        return "error", NET_SessionId
    else:
        #print('登陆成功')
        print("=============>", NET_SessionId)
        return "success", NET_SessionId


def downLoad(id, password):
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
    status, sessionId = login(id, password)
    driver.add_cookie({"name": "ASP.NET_SessionId","value": sessionId})
    cookies = driver.get_cookies()
    print(cookies)
    # NET_SessionId = cookies[0]['value']
    # validateCode = getValidateCode(NET_SessionId)

    # validateCodeUrl = 'http://218.6.132.58/ValidCode.ashx?d=1545442068502'
    # driver.get(validateCodeUrl)
    # validateCode = re.findall("<body>(.*?)</body>", driver.page_source, re.S)[0]

    # time.sleep(5)
    # driver.find_element_by_id('txtUserId-inputEl').send_keys(id)  # 账号
    # driver.find_element_by_id('txtPassword-inputEl').send_keys(password)  # 密码
    # driver.find_element_by_id('txtValid-inputEl').send_keys(validateCode)  # 验证码
    # driver.find_element_by_id('comboGrade-inputEl').send_keys("2014")  # 年级
    # time.sleep(5)
    # driver.find_element_by_id('btnSubmit-btnEl').click()


    downLoadFileUrl = 'http://218.6.132.58/AchievementUpload.aspx?url=AchievementUpload.aspx&_dc=1545467288338&'
    driver.get(downLoadFileUrl)

    time.sleep(4)
    driver.find_element_by_id('button-1023-btnIconEl').click()
    i = 1
    while i < 300:
        time.sleep(1)
        print(id + "<====sleep===>" + str(i))
        i += 1
    driver.close()

def main():
    idAndPasswords = codecs.open('other/idANDpassword.txt', 'r', encoding='utf-8').readlines()[:]
    for idAndPassword in idAndPasswords:
        idAndPasswordArr = idAndPassword.replace('\n', '').split('\t')
        print(idAndPasswordArr)
        id = idAndPasswordArr[0].strip()
        password = idAndPasswordArr[1].strip()
        downLoad(id, password)

if __name__ == '__main__':
    main()





