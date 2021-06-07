# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: list) -> list:
        # Approach 1: Cascading
        #  output = [[]]
        #          for i in (nums):
        #      output += [curr + [i] for curr in output]
        #      print(output)
        #  return output
    

        # Approach 2: Backtracking
        # def backtrack(first = 0, curr = []):
        #     # if the combination is done
        #     if len(curr) == k:  
        #         output.append(curr[:])
        #         return
        #     for i in range(first, n):
        #         # add nums[i] into the current combination
        #         curr.append(nums[i])
        #         # use next integers to complete the combination
        #         backtrack(i + 1, curr)
        #         # backtrack
        #         curr.pop()
        # output = []
        # n = len(nums)
        # for k in range(n + 1):
        #     backtrack()
        # return output


        # Approach 3: Lexicographic (Binary Sorted) Subsets
        n = len(nums)
        output = []
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return output