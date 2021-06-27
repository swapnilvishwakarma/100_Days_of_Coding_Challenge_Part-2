# Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i. 

# All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

# Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

# We want to calculate the probability that the two boxes have the same number of distinct balls.

import math

class Solution:
    def getProbability(self, balls: list) -> float:
        M = len(balls)
        N = sum(balls)
        F = [math.factorial(n) for n in range(N // 2 + 1)]

        s1 = [0] * M
        s2 = [0] * M

        def find(i):
            if i == M:
                if sum(s1) == sum(s2) and len([n for n in s1 if n]) == len([n for n in s2 if n]):
                    base1 = F[N // 2] // math.prod(F[n] for n in s1)
                    base2 = F[N // 2] // math.prod(F[n] for n in s2)
                    return base1 * base2
                return 0

            s = 0
            for n in range(balls[i]+1):
                s1[i] = n
                s2[i] = balls[i] - n
                s += find(i+1)
            return s

        base = math.factorial(N) // math.prod(math.factorial(n) for n in balls)
        return find(0) / base