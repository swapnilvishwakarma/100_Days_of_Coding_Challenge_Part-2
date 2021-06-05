# Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. You can return the output in any order.

class Solution:
    def letterCasePermutation(self, s: str) -> list:
        output = [""]
        
        for c in s:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o + c.lower())
                    tmp.append(o + c.upper())
            else:
                for o in output:
                    tmp.append(o + c)
            
            output = tmp
            
        return output