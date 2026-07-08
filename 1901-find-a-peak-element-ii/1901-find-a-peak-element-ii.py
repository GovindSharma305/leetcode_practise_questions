class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1

        while low <= high:
            mid_col = (low + high) // 2
            max_row = 0
            for row in range(n):
                if mat[row][mid_col] > mat[max_row][mid_col]:
                    max_row = row
            mid_val = mat[max_row][mid_col]
            left_val = mat[max_row][mid_col - 1] if mid_col - 1 >= 0 else -1
            right_val = mat[max_row][mid_col + 1] if mid_col + 1 < m else -1

            if mid_val > left_val and mid_val > right_val:
                return [max_row, mid_col]
            elif left_val > mid_val:
                high = mid_col - 1
            else:
                low = mid_col + 1

        return [-1, -1]