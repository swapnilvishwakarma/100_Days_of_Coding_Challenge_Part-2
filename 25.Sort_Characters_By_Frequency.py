# Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the occurence on each character
        cnt = collections.Counter(s)

        # Build string
        res = []
        for k, v in cnt.most_common():
            res += [k] * v
        print("".join(res))
        return "".join(res)


sol = Solution()
sol.frequencySort('aabCeee')