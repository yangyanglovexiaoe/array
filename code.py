# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    # 使用哈希表的方式，利用字典进行查找，duplication是否为空不能作为判断是由有重复数字的依据，因为duplication不是自己设定的。
    def duplicate(self, numbers, duplication):
        # write code here
        n = len(numbers)
        dic = {}
        for i in range(n):
            if numbers[i] not in dic:
                dic[numbers[i]] = i
            else:
                duplication[0] = numbers[i]
                break
        if len(dic) == n: return False
        else: return True
