# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

class Solution:
    
    def smallestRange(self, nums: list) -> list:
        query = sorted([(n, i) for i, lst in enumerate(nums) for n in lst])
        vM, vm = max(query)[0], min(query)[0]
        minv = vm - 1
        lists = [minv] * len(nums)
        for n, i in query:
            lists[i] = n
            minn, maxn = min(lists), max(lists)
            if minn > minv and (maxn - minn) < vM - vm:
                vM, vm = maxn, minn

        return [vm, vM]