### 09/12/2026
Took me 06:58.15 to finish. Haven't solved in a while.
Here was my solution:

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        map = {}

        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                return True
        
        return False


Wait, looking at my solutions from years ago, it looks like my method is actually correct. Though, I do see myself using hashsets in some solutions. I'll look into that.

I see in the public solutions 3 approaches:
1. Brute force: for every element, check it against every other element that comes after it. If any two match, there is a duplicate. Time complexity is O(n^2). Space complexity is O(1)
2. Sorting: sorting the array makes any duplicate values sit next to each other. So we can compare each element with its immediate neighbor. Time complexity is O(nlogn). Space complexity is O(1).
3. Hashmap: Count how many times each number appears using a hashmap. If any count reaches 2, there is a duplicate. Time complexity: O(n). Space complexity: O(n).


I'm also looking into the difference between a hashmap and hashset.
Hashmap stores key value pairs. Hashset stores only values.

So here are how they are initialized:
### HashMap
my_map = {}

### HashSet
my_set = set()


Here is how hashmaps/dicts are set up:
my_map = {
    5: 0,
    10: 1,
    20: 2
}

Here is how a hashset is:
my_set = {5, 10, 20}


So like hashmaps have values associated to what it is storing while hashsets don't. Further, a hashset contains only unique values (similar to how sets do).

so like:
nums = set()
nums.add(5)
nums.add(10)
nums.add(5)

Adding 5 doesn't create another 5.

Makes sense why we can use this here too.

Something to keep note is hashmap keys also can't be duplicated. Assigning the same key again replaces its old value.