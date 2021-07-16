# Alice plays the following game, loosely based on the card game "21".
# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
# Alice stops drawing numbers when she gets k or more points.
# Return the probability that Alice has n or fewer points.
# Answers within 10-5 of the actual answer are considered accepted.


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        ans = [0]*k + [1]*(n - k + 1) + [0]*maxPts
        val = sum(ans[k: k + maxPts])
        
        for i in reversed(range(k)): 
            ans[i] = val / maxPts
            val += ans[i] - ans[i + maxPts]
            
        return ans[0]