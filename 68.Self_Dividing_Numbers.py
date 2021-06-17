# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list:
        # Method 1
        # result = []
        # for i in range(left, right+1):
        #     for digit in str(i):
        #         if int(digit) == 0 or i % int(digit) != 0:
        #             break
        #     else:
        #         result.append(i)
                    
        # return result

        # Method 2
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        
        result = []
        for n in range(left, right + 1):
            if self_dividing(n):
                result.append(n)
        return result