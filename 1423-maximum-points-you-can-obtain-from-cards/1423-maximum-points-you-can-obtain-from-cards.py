class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        left_sum = 0
        right_sum = 0
        for i in range(0,k):
            left_sum += cardPoints[i]
        maxi = left_sum
        right_ind = n-1
        for i in range(k-1,-1,-1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_ind]
            maxi = max(maxi,left_sum+right_sum)
            right_ind -= 1
        return maxi