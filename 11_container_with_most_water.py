class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        for i in range(len(height)):
            if start == end : break
            max_area = max(max_area, (end - start)  * min(height[start], height[end]))
            
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        return max_area