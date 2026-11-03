class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # 1 1 7 3 12
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        for p,s in pair:
            distance = target - p
            time = distance/s
            stack.append(time)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            
            




        


        
        