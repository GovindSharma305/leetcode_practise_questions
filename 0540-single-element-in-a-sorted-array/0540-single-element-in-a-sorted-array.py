class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1]!= nums[-2]:
            return nums[-1]
        l = 1
        h = n-2

        while l <= h:
            m = (l+h)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if nums[m] == nums[m-1]:
                if m%2 == 1:
                    l = m+1
                else:
                    h = m-1
            else:
                if m%2 == 0:
                    l = m+1
                else:
                    h = m-1
        