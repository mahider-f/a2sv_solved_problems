class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        left, right = 0, len(matrix) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                break  
        
        if not (left <= right):
            return False
        
        row = (left + right) // 2
        
        l, r = 0, len(matrix[0]) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False