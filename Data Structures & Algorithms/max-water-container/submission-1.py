class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = -1
        i,j = 0, len(heights) - 1

        while i < j:
            l = heights[i]
            r = heights[j]
            
            out = max(min(l,r) * (j - i), out)
            if ( l > r):
                j -=1
            else:
                i +=1
        
        return out





            
        