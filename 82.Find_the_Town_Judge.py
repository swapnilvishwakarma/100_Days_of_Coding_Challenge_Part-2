# In a town, there are n people labelled from 1 to n.  There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

class Solution:
    def findJudge(self, n: int, trust: list]) -> int:
        
        trusted = [0] * (n+1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        for i in range(1, n+1):
            if trusted[i] == n-1:
                return i
        return -1