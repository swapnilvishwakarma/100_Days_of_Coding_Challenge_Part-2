# There are n couples sitting in 2n seats arranged in a row and want to hold hands.
# The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).
# Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

from collections import defaultdict

class Solution:
    def minSwapsCouples(self, row: list) -> int:
        n = len(row)
        arr = row
        patner = defaultdict(int) #Stores the patner

        #Populate who is patner
        for i in range(0, n-1, 2):
            patner[i] = i+1
            patner[i+1] = i
        
        ans = 0
        #Traverse the array and swap if not with his/her patner
        for i in range(0, n-2, 2):
            if not patner[arr[i]] == arr[i+1]:
                ans+=1
                temp = arr.index(patner[arr[i]])
                arr[i+1], arr[temp] = arr[temp], arr[i+1]
                
        return ans