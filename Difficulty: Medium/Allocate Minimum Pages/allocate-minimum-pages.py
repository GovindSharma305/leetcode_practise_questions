class Solution:
    def countStudents(self, nums, pages):
        n = len(nums)
        students = 1
        pagesStudent = 0

        for i in range(n):
            if pagesStudent + nums[i] <= pages:
                # Add pages to current student
                pagesStudent += nums[i]
            else:
                # Add pages to next student
                students += 1
                pagesStudent = nums[i]

        return students

    def findPages(self, arr, k) -> int:
        n = len(arr)

        # Book allocation impossible
        if k > n:
            return -1

    
        low = max(arr)
        high = sum(arr)

        while low <= high:
            mid = (low + high) // 2
            if self.countStudents(arr, mid) <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low