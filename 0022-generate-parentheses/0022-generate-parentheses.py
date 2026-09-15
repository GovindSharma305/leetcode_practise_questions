class Solution:
    def solve(self,ind,brackets,total,result):
        if ind >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        if total > len(brackets)//2:
            return
        if total < 0:
            return
        brackets[ind] = "("
        sum = total + 1
        self.solve(ind+1,brackets,sum,result)
        brackets[ind] = ")"
        sum = total -1
        self.solve(ind+1,brackets,sum,result)

    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        brackets = [""]*(n*2)
        self.solve(0,brackets,0,result)
        return result