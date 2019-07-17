# -*- coding: utf-8 -*-
'''
判断一组数字是否连续
'''

nums = [1,3,5,4,2,7,10]
nums.sort()
print("排序后: %s" % ( nums))





index = 0
for i in nums:

    if index == len(nums)-1:
        break
    r1 = nums[index +1]
    r2 = nums[index]
    index = index + 1

    r = r1 - r2
    # print(r)
    if  r >  1:
        print( "%d 前缺失 %d个标识  " % (nums[index], r-1)  )

