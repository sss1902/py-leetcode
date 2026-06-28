# 两数之和 暴力解法时间复杂度为On2
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力解法
        result:List[int] = []
        for i in range(len(nums)):
            for j+1 in range(len(nums)):
                if nums[i]+nums[j] == target and i != j:
                    result.append(i)
                    result.append(j)
                    return result



# 两数之和 使用hash表 bug版 未考虑自己加上自己
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        result:List[int] = []
        for i,value in enumerate(nums):
            # 添加字典
            # 为啥要这样写，因为字典只能通过key快速找到value，不能通过value快速找到key(必须遍历)
            hash_table[value] = i
        for i,value in enumerate(nums):
            another = target-value
            # 判断值是否在字典中
            # if another in hash_table.values() # 这种是判断一个值是否在values中
            if another in hash_table:  # 会出现一个严重的bug,自己+自己
                result.append(i)
                result.append(hash_table[another])
                return result

# 两数之和 
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        # 遍历列表
        for i,value in enumerate(nums):
            # 先查
            another = target-value
            if another  in hash_table : # 如果另一个数在hash表中
                return [i,hash_table[another]]  # 直接返回
            # 如何另一个不在就将这个数存入hash表中
            hash_table[value]= i
        return []
