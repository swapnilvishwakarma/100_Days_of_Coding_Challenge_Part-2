# n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:

# Take their own seat if it is still available, 
# Pick other seats randomly when they find their seat occupied 
# What is the probability that the n-th person can get his own seat?


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        else:
            return 0.5