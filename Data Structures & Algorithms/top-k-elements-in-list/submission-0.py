class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for x in nums:
            count[x] = 1 + count.get(x,0)
        
        for n,f in count.items():
            freq[f].append(n)
        
        res = []
        for i in range (len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (k == len(res)):
                    return res
            
            




