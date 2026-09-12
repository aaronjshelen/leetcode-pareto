# Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.

from typing import List # just to get rid of squiggle line

# Hashset implementation
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False

# Hashmap implementation
class Solution(object):
    def containsDuplicate(self, nums):
        
        map = {}

        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                return True
        return False