class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_set = set(nums)
        longest = 0

        for num in nums_set:

            # Only start if num is the beginning of a sequence
            if num - 1 not in nums_set:
                current = num
                length = 1

                # Count consecutive numbers
                while current + 1 in nums_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest