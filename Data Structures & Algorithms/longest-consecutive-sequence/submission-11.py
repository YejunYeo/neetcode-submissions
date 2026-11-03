class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         if (nums == []):
            return 0
         em_set = set()
         for i in range(len(nums)):
            em_set.add(nums[i])
         maxi = 1
         for num in em_set:
            if (num - 1) not in em_set:
               length = 1
               while (num + length) in em_set:
                  length+=1
                  maxi = max(maxi, length)
         
         return maxi


                  


            

         



         

                
            



         

