# Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.

class Solution:
    def xorQueries(self, arr: list, queries: list) -> list:
        
        res = [arr[0]]
        for i in arr[1:]:
            res.append(res[-1]^i)
        
        res.append(0)
        return [res[L-1]^res[R] for L, R in queries]