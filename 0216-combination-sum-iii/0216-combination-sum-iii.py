class Solution:
    def func(self,n,sum,last,nums,k,ans):
        if sum == n and len(nums) == k:
            ans.append(list(nums))
            return
        if sum > n or len(nums) > k:
            return
        
        for i in range(last,10):
            nums.append(i)
            self.func(n,sum+i,i+1,nums,k,ans)
            nums.pop()

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        nums = []
        self.func(n,0,1,nums,k,ans)
        return ans
        