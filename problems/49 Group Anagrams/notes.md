### 09/17/2026

I got the main idea down, just my syntax and understanding of python was bad.

Didn't know that lists can't be dict keys.
So tuples are used instead.

My solution:
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hm = {} # key = anagram word, value = list of og words

        for le_str in strs:
            
            # if le_str is anagram:
            #       add it to appropriate key in hashmap
            key = tuple(sorted(le_str))
            if key not in hm:
                hm[key] = []
            hm[key].append(le_str)
           
            
        return hm.values()


But apparently the optimal approach is to use a 26-character frequency count as the hashmap key instead of sorting every string:
def groupAnagrams(strs):
    hashmap = {}

    for s in strs:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        key = tuple(count)

        if key not in hashmap:
            hashmap[key] = []

        hashmap[key].append(s)

    return list(hashmap.values())