# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution:
    def maximum69Number (self, num: int) -> int:
        # Method 1
        # num = str(num)
        # for i, val in enumerate(num):
        #     if int(val) == 6:
        #         num = num.replace(val, '9', 1)
        #         break
        # return num
    
        # Method 2
        return (int(str(num).replace("6","9",1)))