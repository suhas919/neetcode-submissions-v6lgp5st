from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        p, q = min(piles), max(piles)

        if len(piles) == 1:
            return ceil(piles[0]/h)
        def diff(k):
            res = 0
            for i in range(len(piles)):
                res += ceil(piles[i]/k)
            return h - res



        n,m = 1,q
        res = max(piles)
        while n <= m:

            mid = (n+m)//2
            #print(n,m,mid,mid)
            if diff(mid) >= 0:
                m = mid - 1
                res = mid
            else:
                n = mid+1

        return res


        