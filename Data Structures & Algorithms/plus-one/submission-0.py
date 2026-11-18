class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        multiplier = 1 * ( 10 ** (len(digits) - 1))
        sum1 = 0
        for i in range(len(digits)):
            sum1 += (multiplier * digits[i])
            multiplier //=10
        
        str1 = str(sum1 + 1)
        return list(str1)

            

