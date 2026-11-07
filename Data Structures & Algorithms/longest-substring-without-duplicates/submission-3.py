class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        em_set = set()
        counter = 0
        maximum = 0
        left = 0


        for i in range (len(s)):
            while s[i] in em_set:
                em_set.remove(s[left])
                left +=1
            em_set.add(s[i])
            maximum = max(maximum, (i - left) + 1)


            

        return maximum
                



