class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sizeof window - maxf <= k
        # The window can only grow that is the ke
        # L = size of window
        # maxf = f

        # The window will shift right if L - f > k
        # if L-f > k then it means there are more chars that need to be replaced
        # but the previous valid window
        # will be of length L where L - f = k
        # when the window shifts, L will be the same length
        # if maxf becomes smaller:
        # For example [A,A,A,B,A], moves to [A,A,B,A,B] where k is 1
        # the window has shifted will become immediately invalid
        # so the maxf can only increase or stay the same
        
        count = {}
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            
            while (r - l + 1) - maxf > k:
                count[s[l]] -=1
                l+=1
            res = max(res, r - l +1)
        return res


            
            

        
                

                
                

                
        


        return max(counter,maximum)
            

            


