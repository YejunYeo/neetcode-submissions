class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while (left <= right):
            mid_row = (right + left) // 2
            if (matrix[mid_row][0] > target):
                right = mid_row - 1
            elif (target > matrix[mid_row][-1]):
                left=mid_row+1
            else:
                break
        row = mid_row

        arr = matrix[row]
        l,r = 0, len(arr) - 1
        while (l<=r):
            mid = (l + r)//2
            if (arr[mid] == target):
                return True
            elif(target > arr[mid]):
                l= mid+1
            else:
                r= mid-1
        
        return False
        

        # when target is between the first col and last col then the we have found the row
        # we break when its in between
        # we look for other rows when
        # if target < first col, 
        # if target > first col but target larger than the last col,
