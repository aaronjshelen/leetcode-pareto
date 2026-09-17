### 09/17/2026
Didn't time myself doing this one,
but I actually solved it pretty quickly.

Here was my solution:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hm = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hm:
                return (hm[complement], i)
            else:
                hm[nums[i]] = i

        return None



I need to study the for-loop variations in python.

 