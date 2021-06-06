# You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.
# Return the number of good splits you can make in s.

# from collections import Counter
# class Solution:
#     def numSplits(self, s: str) -> int:
#         length = len(s)
#         out = 0
#         for i in range(length):
#             p, q = "", ""
#             p += s[:i+1]
#             q += s[i+1:]
#             if p and q:
#                 p_ = Counter(p)
#                 q_ = Counter(q)
#                 if len(p_) == len(q_):
#                     out += 1
#         return out
    

# Faster
from collections import defaultdict
class Solution:
    def numSplits(self, s: str) -> int:
        leftDict = defaultdict(lambda: 0)
        rightDict = defaultdict(lambda: 0)
        splits = 0
        for i in set(s):
            rightDict[i] = s.count(i)
        for i in s:
            leftDict[i] += 1
            rightDict[i] -= 1
            if(rightDict[i] == 0):
                del rightDict[i]
            if(len(leftDict) == len(rightDict)):
                splits += 1
        return splits