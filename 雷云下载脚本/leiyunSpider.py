#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2018/12/8 14:02
@Author  : Negen
@Site    : 
@File    : leiyunSpider.py
@Software: PyCharm
'''
import codecs

import requests
import json
import os

headers = {
    'Host': 'www.leiyun.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://www.leiyun.org/sf/8a9f0eb75aced5731b91fc109c9aba44.html',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    # 'Cookie': '__cfduid=dd2d3d64cfea20993d49e82f3a45bdbde1543563785; Hm_lvt_1b6ff5a098bf9ea637b1509f4c3a5cdb=1543564003,1544248309; PHPSESSID=lqhu7fpisbafmthrdmtncqdjn3; Hm_lpvt_1b6ff5a098bf9ea637b1509f4c3a5cdb=1544248309'
}

base_url = 'https://www.leiyun.org/sf/8a9f0eb75aced5731b91fc109c9aba44.html'
request = requests.Session()
request.get(base_url, headers = headers)
firstFloder_url = 'https://www.leiyun.org/share/folderAction.php?list=Khg3egVI254FbNb08RL0H9EC5RsI706PyCYawlKgpZS4adLDp8AeLN3CwE4evhs&hash=8a9f0eb75aced5731b91fc109c9aba44&referrer='
floder_base_url = 'https://www.leiyun.org/share/folderAction.php?hash=8a9f0eb75aced5731b91fc109c9aba44&referrer=&list='
response = request.get(firstFloder_url, headers = headers).text
responseJson = json.loads(response)
dataArr = responseJson.get('data')



def jsonData(path):
    try:
        resp = request.get(floder_base_url + path, headers=headers).text
        respJsonDatas = json.loads(resp).get('data')
        for t in respJsonDatas:
            print(t)
        return respJsonDatas
    except:
        return jsonData(path)





baseDir = 'E:/雷云/'
def openFloder(Datas, dirPath):
    for data in Datas:
        server_filename = data.get('server_filename')
        if data.get('isdir') == 1:
            # resp = request.get(floder_base_url + data.get('path'), headers = headers).text
            respJsonDatas = jsonData(data.get('path'))

            desPath = dirPath + server_filename + '/'
            if not os.path.exists(desPath):
                os.makedirs(desPath)
                print('创建文件夹===>' + server_filename)
            openFloder(respJsonDatas, desPath)
        else:
            try:
                hashCode = '8a9f0eb75aced5731b91fc109c9aba44'
                downloadPath = data.get('path')
                downloadPostUrl = 'https://www.leiyun.org/share/folderAction.php?down={0}&folderDown=1&hash={1}'.format(
                    downloadPath,
                    hashCode)

                _headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
                    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    'Host': 'd10.baidupcs.com',
                    'Upgrade-Insecure-Requests': '1',
                    # 'Cookie': '__cfduid=dd2d3d64cfea20993d49e82f3a45bdbde1543563785; Hm_lvt_1b6ff5a098bf9ea637b1509f4c3a5cdb=1543564003,1544248309; PHPSESSID=lqhu7fpisbafmthrdmtncqdjn3; Hm_lpvt_1b6ff5a098bf9ea637b1509f4c3a5cdb=1544248309'
                }


                if os.path.exists(dirPath + server_filename):
                    print(dirPath + server_filename+ "已存在")
                    pass
                else:
                    resp = request.get(downloadPostUrl, headers=headers).text
                    downloadUrl = 'https://www.leiyun.org/director.html#!' + json.loads(resp).get('url')
                    print(data.get('server_filename'), downloadUrl)
                    downloadUrl = json.loads(resp).get('url')
                    print('downloading ' + server_filename)
                    sourceData = request.get(downloadUrl, headers=_headers).content
                    with open(dirPath + server_filename, "wb") as code:
                        code.write(sourceData)
                        print("写入>>" + dirPath + server_filename + "<<完成")
            except:
                #下载失败
                with codecs.open('error40.txt', 'a', encoding='utf-8') as f:
                    f.write(dirPath + server_filename + '\n')

openFloder(dataArr[65:],baseDir)

# print(dataArr)


# for data in dataArr:
#     if data.get('isdir') == 1:
#         resp = request.get(floder_base_url + data.get('path'), headers = headers).text
#         respJsonDatas = json.loads(resp).get('data')
#         for respJson in respJsonDatas:
#             if respJson.get('isdir') == 1:
#                 resp = request.get(floder_base_url + data.get('path'), headers=headers).text
#                 respJsonDatas = json.loads(resp).get('data')
#                 print(respJsonDatas)
#                 exit(0)
















"""
获取下载链接
"""
def download(path):

    hashCode = '8a9f0eb75aced5731b91fc109c9aba44'
    path = 'IBhhdgUd2JkFbNb08RL0H9EC5RsI706PyCYawlKgpZS4adLDp8AeLN3CwE4evhsBUfP_bpLygt1_bI7SKWW7R63iJkx9oOc6MJaltCZvYhOR4cSo0FPWADrCMdmOzZDvERITOMdyYaraE2g4A'
    url = 'https://www.leiyun.org/share/folderAction.php?down={0}&folderDown=1&hash={1}'.format(path, hashCode)
    response = requests.get(url, headers = headers).text
    ccookies = requests.get(url, headers = headers).cookies
    if '' != response:
        downLaodUrl = json.loads(response)['url']
        print(downLaodUrl)

        r = requests.get(downLaodUrl, headers=headers, cookies = ccookies)
        print(r.text)
        # with open("text.avi", 'wb') as f:
        #     f.write(r.content)

# download('')

