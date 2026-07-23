class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def csi(goal):
            if goal<0:
                return 0
            left = 0
            right = 0
            total = 0
            count = 0
            while right<n:
                total += nums[right]
                while total>goal:
                    total -= nums[left]
                    left += 1
                count += ((right-left)+1)
                right += 1
            return count
        return csi(goal)-csi(goal-1)

        