class Solution:
    def solve(self, index: int, subset: List[int], nums: List[int], result: List[List[int]]):
        if index >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        self.solve(index+1,subset,nums,result)
        subset.pop()
        self.solve(index+1,subset,nums,result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(0,[],nums,result)
        return result
        