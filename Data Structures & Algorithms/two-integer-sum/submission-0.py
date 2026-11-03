class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate (nums):
            diff = target - value
            if diff in hashmap:
                arr = [hashmap[diff], index]
                return arr
            else:
                hashmap[value] = index
        