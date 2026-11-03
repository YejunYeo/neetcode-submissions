class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, f in enumerate(temperatures):
            while stack and f > stack[-1][0]:
                sf, si = stack.pop()
                diff = i - si
                res[si] = diff
            stack.append((f,i))
        
        return res






        




        
        