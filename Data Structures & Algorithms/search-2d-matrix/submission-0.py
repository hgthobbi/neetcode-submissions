class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][-1]:
                start = mid + 1
            else:
                newStart = 0
                newEnd = len(matrix[0]) -1
                while newStart <= newEnd:
                    newMid = (newStart + newEnd) // 2
                    if target < matrix[mid][newMid]:
                        newEnd = newMid - 1
                    elif target > matrix[mid][newMid]:
                        newStart = newMid + 1
                    else:
                        return True
                return False
        return False
        