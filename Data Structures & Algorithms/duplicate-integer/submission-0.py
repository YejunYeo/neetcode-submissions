class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        my_set = set()
        for i in range(len(nums)):
            my_set.add(nums[i])
        length_of_set = len (my_set)
        if (length_of_set != len(nums)):
            return True
        else:
            return False