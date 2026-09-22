09/22/2026

I had the correct idea, but the syntax for the for loop made it incorrect.

Here was my passing solution:
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        occurences = {}
        top_k = []
        for i in nums:
            if i not in occurences:
                occurences[i] = 1
            else:
                occurences[i] += 1
        
        for j in range(k):
            largest = max(occurences, key=occurences.get)
            top_k.append(largest)
            del occurences[largest]


        return top_k


        
I'll look into the optimal solution and include it in solution.py.

Bucket sort looks to be the move here.