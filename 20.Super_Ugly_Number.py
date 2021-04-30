# A super ugly number is a positive integer whose prime factors are in the array primes.
# Given an integer n and an array of integers primes, return the nth super ugly number.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        N, m, S = [1], 1, set()
    	
        for _ in range(n):
            while m in S:
                m = heapq.heappop(N)
            S.add(m)
            for i in primes:
                heapq.heappush(N, i*m)
                
        return m