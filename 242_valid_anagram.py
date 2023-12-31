from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = {}

        # count the frequency of characters in string s
        for x in s:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        # count the frequency of characters in string t
        for x in t:
            if x in count:
                count[x] -= 1
            else:
                count[x] = 1
        
        for val in count.values():
            if val != 0:
                return False
        return True

result = Solution()
print(result.isAnagram("car", "rat"))