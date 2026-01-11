class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
            
        return max_area
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] 
        max_a = 0
        heights_with_sentinel = heights + [0]
        
        for i, h in enumerate(heights_with_sentinel):
            start_index = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                width = i - idx 
                max_a = max(max_a, height * width)
                start_index = idx 
            stack.append((start_index, h))
            
        return max_a