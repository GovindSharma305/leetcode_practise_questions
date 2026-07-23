class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def csi(goal):
            if goal<0:
                return 0
            left = 0
            right = 0
            total = 0
            count = 0
            while right<n:
                total += nums[right]%2
                while total>goal:
                    total -= nums[left]%2
                    left += 1
                count += ((right-left)+1)
                right += 1
            return count
        return csi(k)-csi(k-1)