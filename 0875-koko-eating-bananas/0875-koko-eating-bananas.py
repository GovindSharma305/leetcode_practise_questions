import math
class Solution:
    def totalhours(self,piles,h_rate):
        total = 0
        for i in range(0,len(piles)):
            total = total + math.ceil(piles[i]/h_rate)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = -1
        while low<=high:
            mid = (low+high)//2
            t_h = self.totalhours(piles,mid)
            if t_h <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        
    

        