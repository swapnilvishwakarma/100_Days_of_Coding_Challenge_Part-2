# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        times = ''
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            times = '-'
            numerator = abs(numerator)
            denominator = abs(denominator)
        if numerator < 0 and denominator < 0:
            numerator = -numerator
            denominator = -denominator
        decimal = []
        remainders = []
        
        while True:
            decimal.append(str(numerator // denominator))
            numerator %= denominator
            remainders.append(numerator)
            numerator *= 10
            
            if numerator == 0:
                if len(decimal) == 1:
                    return times + ''.join(decimal)
                return times + decimal[0] + '.' + ''.join(decimal[1:])
            
            if remainders.count(remainders[-1]) > 1:
                decimal.insert(remainders.index(remainders[-1]) + 1, '(')
                decimal.append(')')
                return times + decimal[0] + '.' + ''.join(decimal[1:])