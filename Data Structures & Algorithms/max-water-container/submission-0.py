class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = -1

        length = len(heights)

        while (length >= 2):
            l = heights[0]
            r = heights[-1]
            compute = (min(l,r)) * (length - 1)
            out = max(out, compute)
            if l > r:
                heights.pop()
                length -=1

            elif r > l:
                heights.pop(0)
                length -=1
            elif r == l and length <=3:
                heights.pop()
                length -=1
            elif r == l and length > 3:
                if (heights[1] > heights[-2]):
                    heights.pop(0)
                    length -=1
                else:
                    heights.pop()
                    length-=1
        return out
    


            
        