class Solution:
    def bs(self,nums,target):
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return False






    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        for i in range(0,r):
            if matrix[i][0] <= target and matrix[i][c-1] >= target:
                ind = self.bs(matrix[i],target)
                if ind:
                    return True
        return False