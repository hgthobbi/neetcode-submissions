class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        left, right = 0, len(heights) - 1
        while left < right:
            currAmount = (right - left) * min(heights[left], heights[right])
            maxAmount = max(currAmount, maxAmount)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxAmount
        