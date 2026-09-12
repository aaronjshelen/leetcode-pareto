### 09/12/2026
05:18.13

Pretty straightforward.

My solution:
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}


        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] += 1

            if t[i] not in hash_t:
                hash_t[t[i]] = 1
            else:
                hash_t[t[i]] += 1            

        if hash_s == hash_t:
            return True
        else:
            return False


Something I noticed is that I really forgot the different syntaxes for Python. Like the for-loop could have been simply: `for i in s` rather than iterating through the length of the string.