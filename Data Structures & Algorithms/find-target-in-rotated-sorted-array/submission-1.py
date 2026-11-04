class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minimum = 1001
        l = 0
        r = len(nums) - 1
        while (l < r):
            mid = (l + r) //2
            if (nums [r] > nums[mid]):
                r = mid
            else:
                l = mid + 1

        pivot = l

        def bsearch(lo, hi):
            while (lo <= hi):
                mid = (lo + hi)//2
                if (nums[mid] == target):
                    return mid
                elif (nums[mid] > target):
                    hi = mid -1
                else:
                    lo = mid + 1
            return -1


        res = bsearch(0, pivot-1)

        if (res != -1):
            return res
        
        return bsearch(pivot, len(nums) - 1)
        




        # I find the minimum, cuz thats where 2 arrays become clear
        # then I run binary search
    
