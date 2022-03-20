'''You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, 
such that the container contains the most water.
Return the maximum amount of water a container can store.'''


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