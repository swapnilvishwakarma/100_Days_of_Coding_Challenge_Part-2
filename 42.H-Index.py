# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.
# If there are several possible values for h, the maximum one is taken as the h-index.

class Solution:
    def hIndex(self, citations: list) -> int:
        
        citations.sort( reverse = True )
        for idx, citation in enumerate(citations):
            if idx >= citation:
                return idx
        
        return len(citations)