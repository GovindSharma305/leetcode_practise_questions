class Solution:
    def solve(self, nums, total, index, result):
        # Base case: processed all elements
        if index >= len(nums):
            result.append(total)  # Add current running total
            return

        # Choice 1: Include current element (add to running total)
        Sum = total + nums[index]
        self.solve(nums, Sum, index + 1, result)

        # Choice 2: Exclude current element (keep same total)
        Sum = total  # This line is actually redundant
        self.solve(nums, Sum, index + 1, result)

    def subsetSums(self, arr):
        result = []
        self.solve(arr, 0, 0, result)  
        result.sort()
        return result