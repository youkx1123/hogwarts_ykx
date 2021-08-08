"""
"第一个只出现一次的字符"
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中
找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.（从0开始计数）
"""

# -*- coding:utf-8 -*-
from _ctypes_test import func

from pip._vendor.distlib.compat import raw_input


class Solution:
    def FirstNotRepeatingChar(self, s):
        for i in s:
            if s.count(i) == 1:
                print(s.index(i))
        return -1
    while 1:
        try:
            print(func(raw_input()))
        except:
            break

    # while -1:
    #     try:
    #         print(func(raw_input()))
    #     except:
    #         break


