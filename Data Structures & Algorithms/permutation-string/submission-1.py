class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # the brute foce way would be 
        # get all permutations of s1 and check if any of the perutations is 
        # in s2

        # maybe create a sliding window of length(s1) and check if they are unique?
        # can I check if a set is indetical?
        # time would be len(s1) * len(s2 - s1)

        l1 = len(s1)
        l2 = len(s2)
        e1 = {}
        e2 = {}

        for i in range (len(s1)):
            e1[s1[i]] = e1.get(s1[i], 0) + 1

        # 3 7
        # lec, eca, cab, abe, bee

        for i in range (l2 - l1 + 1):
            for j in range (l1):
                e2[s2[i+j]] = e2.get(s2[i+j], 0) + 1
            if (e2 == e1):
                return True
            else:
                e2 = {}
                continue
        return False





