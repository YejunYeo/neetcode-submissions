class Solution:
    def findMin(self, nums: List[int]) -> int:

        minimum = 1001
        l = 0
        r = len(nums) - 1
        while (l<= r):
            mid = (l + r) // 2
            if (nums[mid] < nums[r]):
                r = mid - 1
                minimum = min(nums[mid], minimum)
            else:
                l = mid + 1
                minimum = min(nums[mid], minimum)
        
        return minimum






