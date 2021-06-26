# You are given an even integer n​​​​​​. You initially have a permutation perm of size n​​ where perm[i] == i​ (0-indexed)​​​​.

# In one operation, you will create a new array arr, and for each i:

# If i % 2 == 0, then arr[i] = perm[i / 2].
# If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].
# You will then assign arr​​​​ to perm.

# Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1
        mod = n - 1
        curr_power = 2
        cnt = 1
        
        # Find multiplicative order modulo n-1
        while curr_power != 1:
            curr_power = (2*curr_power) % mod
            cnt += 1
        return cnt