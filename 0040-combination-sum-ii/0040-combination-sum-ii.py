class Solution:
    def solve(self,subset,index,target,result,candidates):
        if target == 0:
            result.append(subset.copy())
            return
        for i in range(index,len(candidates)):
            if i>index and candidates[i] == candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            subset.append(candidates[i])
            self.solve(subset,i+1,target-candidates[i],result,candidates)
            subset.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        self.solve([],0,target,result,candidates)
        return result        