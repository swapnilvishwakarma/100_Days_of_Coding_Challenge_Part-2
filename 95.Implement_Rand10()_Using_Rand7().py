# Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.
# Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().

# Follow up:
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?

# Example 1:
# Input: n = 1
# Output: [2]

# Example 2:
# Input: n = 2
# Output: [2,8]

# Example 3:
# Input: n = 3
# Output: [3,8,10]


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import math

class Solution:
    def rand7(self):
        return math.random.randint(1, 7)

    def rand10(self):
        """
        :rtype: int
        """
        curr = 40
        while curr >= 40:
            curr = (self.rand7() - 1) * 7 + self.rand7() - 1
        return curr % 10 + 1