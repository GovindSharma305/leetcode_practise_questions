class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0
        stack = []

        for brac in s:
            if brac == "(":
                stack.append(brac)
                curr_depth += 1
                max_depth = max(max_depth,curr_depth)
            elif brac == ")":
                curr_depth -= 1
                stack.pop()
        return max_depth
        