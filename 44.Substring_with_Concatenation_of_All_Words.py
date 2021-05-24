# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
# You can return the answer in any order.

import collections

class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if not words:
            return []
        
        LS, M, N, C = len(s), len(words), len(words[0]), collections.Counter(words)
        return [i for i in range(LS-M*N+1) if collections.Counter([s[a:a+N] for a in range(i,i+M*N,N)]) == C]