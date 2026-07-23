class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        i = 0
        numbers = {"a": -1, "b": -1, "c": -1}
        while i < n:
            numbers[s[i]] = i
            if numbers["a"] >= 0 and numbers["b"] >= 0 and numbers["c"] >= 0:
                count += min(numbers.values()) + 1
            i += 1
        return count