class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        first, last = 0, rows - 1

        while first <= last:
            row = (first + last) // 2
            
            if target > matrix[row][-1]:
                first = row + 1
            elif target < matrix[row][0]:
                last = row - 1
            else:
                break

        if not (first <= last):
            return False

        row = (first + last) // 2
        left, right = 0, cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        
        return False