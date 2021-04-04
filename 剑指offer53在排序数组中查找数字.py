#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/4/4 10:51
# @Author : CN-JackZhang
# @File: 剑指offer53在排序数组中查找数字.py

def search(nums, target: int):
    # 计数函数
    # def cnt(nums,target):
    #     n = 0
    #     for i in range(len(nums)):
    #         if target in nums and target == nums[i]:
    #             n += 1
    #     return n
    if target in nums:
        return nums.count(target)
        # return cnt(nums,target)
    else:
        return 0

nums = [5,7,7,8,8,10]
target = 8
test = search(nums,target)
print(test)