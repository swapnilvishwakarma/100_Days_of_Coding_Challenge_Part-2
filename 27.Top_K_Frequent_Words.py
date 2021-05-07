# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        dict = {}
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        
        res = sorted(dict, key = lambda x: (-dict[x], x))
        print(res[:k])
        return res[:k]

sol = Solution()
sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2)