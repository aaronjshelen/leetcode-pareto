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



        