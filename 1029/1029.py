#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 1029.py
# @Author: Negen
# @Date  : 2018/10/29/029
# @Desc  :


from random import randint
from collections import Counter

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
print(countNum())