class Solution:

    def twoSum(self, nums, target):
        d = {}
        result =[]
        for i,num in enumerate(nums):
            temp = target = num
            if temp in d:
                result.append(d[temp])
                result.append(i)

            d[num] =i
        return result
