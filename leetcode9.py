class Solution(object):
  def twoSum(self, nums, target):
    Hashmap = {}
    for index , value in enumerate(nums):  
      key = target - value 
      if key in Hashmap:
        return [Hashmap[key], index]
      else:
        Hashmap[value] = index
