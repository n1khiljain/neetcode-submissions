class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while (left <= right): # find row to iterate over
            mid = (left + right) // 2

            inner_l, inner_r = 0, len(matrix[mid]) - 1

            while (inner_l <= inner_r): #iterate through each row
                mid_two = (inner_l + inner_r) // 2

                if matrix[mid][mid_two] == target:
                    return True
                elif matrix[mid][mid_two] < target:
                    inner_l = mid_two + 1
                else:
                    inner_r = mid_two - 1
            
            if matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


            