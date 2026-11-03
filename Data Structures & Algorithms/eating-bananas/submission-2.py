class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # I got this question wrong because I didn't think of brute force solution first


        # 1 to largest = speed

        # [1, ... , max] if we f(speed) > h, then we look at thr RHS

        # else, look at the left hand side and see if there is anything smaller

        l = 1
        r = max(piles)
        minimum = max(piles)

        while l <= r:
            mid = (l + r)//2
            summ = 0
            for i in range (len(piles)):
                summ += -(-piles[i]//mid)
            
            if (summ > h):
                l = mid + 1
            
            else:
                minimum = min(mid, minimum)
                r = mid - 1
            #1....25
        
        return minimum

                

                








