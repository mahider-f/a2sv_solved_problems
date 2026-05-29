class Solution:
    def getSkyline(self, buildings):
        
        points = []
        for left, right, height in buildings:
            points.append((left, -height))  
            points.append((right, height))  
        points.sort()
        heights = [0]  
        skyline = [(0, 0)]  

        for x, h in points:
            if h < 0:
                heapq.heappush(heights, h)  
            else:
                heights.remove(-h)  
                heapq.heapify(heights)  
            max_height = -heights[0]
            if max_height != skyline[-1][1]:
                skyline.append((x, max_height))

        return skyline[1:]