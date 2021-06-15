# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

import numpy as np
from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Using eval
        return eval('*'.join(str(n))) - eval('+'.join(str(n)))
        
        # Using numpy
        # a = [int(x) for x in str(n)]
        # return np.prod(a) - np.sum(a)
        
        # Using reduce
        # a = [int(x) for x in str(n)]
        # return reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x + y), a)