# Solution : In python 3

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        f=v[0]
        l=v[-1]
        for i in range(min(len(f),len(l))):
            if(f[i]!=l[i]):
                return ans
            ans+=f[i]
        return ans
        
# driver code for running 
"""
s = Solution()

plist = ["flower", "flow", "flight"]

outputlist = s.longestCommonPrefix(plist)

print(outputlist)
"""
# 

# Explanation : line by line
# The code starts by creating a list that will store all the characters in both strings.
# Then, it sorts them and stores the first character in one string as 0 and last character in another string as -1.
# It then iterates through each index of both lists until it finds a mismatch between the two lists (a difference between their first or last characters).
# The code then returns an empty string if there is no match found, otherwise it adds up all the characters from its own list and appends those to itself.
# The code will return the longest common prefix of the input list.

