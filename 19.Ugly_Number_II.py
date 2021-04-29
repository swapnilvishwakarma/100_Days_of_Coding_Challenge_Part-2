# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums_list = [1]
        
        two_position = 0
        three_position = 0
        five_position = 0
        
        while len(ugly_nums_list) < n:
            by2 = ugly_nums_list[two_position]*2
            by3 = ugly_nums_list[three_position]*3
            by5 = ugly_nums_list[five_position]*5
            
            minimum = min(by2, by3, by5)
            ugly_nums_list.append(minimum)
            
            if minimum == by2:
                two_position += 1
            if minimum == by3:
                three_position += 1
            if minimum == by5:
                five_position += 1

        print(ugly_nums_list[-1])        
        return ugly_nums_list[-1]

sol = Solution()
sol.nthUglyNumber(10)