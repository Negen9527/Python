#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 1029.py
# @Author: Negen
# @Date  : 2018/10/29/029
# @Desc  :


from random import randint
from collections import Counter
import re


"""
统计一百个0-9之间的随机整数各自出现的次数，返回字典
结果：{6: 18, 3: 7, 1: 7, 9: 10, 2: 9, 8: 13, 7: 9, 0: 10, 5: 8, 4: 9}
"""
def countNum():
    numList = []
    for i in range(0, 100):
        num = randint(0, 9)
        numList.append(num)
    result = Counter(numList)
    retDict = {k: v for k, v in sorted(result.items(), key=lambda k: k[0], reverse=False)}
    return retDict
print("随机数出现次数字典：", countNum())


"""
处理字符串
a = 'aAsmr3idd4bgs7Dlsf9eAF'
"""
def handleStr(sourceStr):
    print("输入的字符串为：", sourceStr)
    #a提取字符串中的数字组成新串
    numStr = "".join(re.findall('[\d+]', sourceStr))

    print("提取的数字字符串为：",numStr)
    
    """
    #b.统计字符串中的字母出现的次数，输出字典
    """
    #提取非数字的字符并转换为小写字母
    notNumList = [ch.lower() for ch in re.findall('[^\d+]', sourceStr)]            

    #统计各个字母出现的次数并按字母升序排列
    result = sorted(Counter(notNumList).items(), key=lambda k:k[0], reverse=False)
    countNumDic =  {k:v for k,v in result}
    print("各字符出现的次数：", countNumDic)

    """
    #c.字符去重
    """

    sourceStrList = [ch.lower() for ch in list(sourceStr)]
    tempStr = "".join(sourceStrList)
    #去重
    for index,ch in enumerate(sourceStrList):
        if ch.isdigit():
            pass
        else:
           if ch in tempStr[index + 1:]:
               tempStr = tempStr[:index + 1] + tempStr[index + 1:].replace(ch, ' ')
    tempStr = tempStr.replace(' ', '')
    print("去重后的字符串：", tempStr)
    

a = 'aAsmr3idd4bgs7Dlsf9eAF'
handleStr(a)