#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/4/4 7:29
# @Author : CN-JackZhang
# @File: 44.py
'''用快速排序对字典'''

def quick_sort(nums):
    if not nums:
        return []
    tmp = nums[0]
    left = []
    right = []
    for i in range(1, len(nums)):
        if nums[i] < tmp:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return quick_sort(left) + [tmp] + quick_sort(right)

def topKFrequent(nums, k):
    # 快速排序
    ans = quick_sort(nums)
    set_ans = set(ans)
    #定义一个空字典来存储每一个元素对应的次数
    ele_dict = {}
    for i in set_ans:
        #用count统计对应元素的次数
        ele_dict[i] = ans.count(i)
    #{1: 1, 2: 2, 3: 1, 4: 1, -1: 2}
    #对字典按照value排序,返回1个列表，降序
    time = sorted(ele_dict.items(),key=lambda d:d[1], reverse=True)
    #用一个计数器，取前k个元素
    n = 0
    res = []
    for key in time:
        if n < k:
            #把相应元素存入res列表
            res.append(key[0])
            n += 1
    return res

# nums = [1,1,1,2,2,3]
nums = [4,1,-1,2,-1,2,3]
k = 2
# ans = quick_sort(nums)
ans = topKFrequent(nums,k)
print(ans)
