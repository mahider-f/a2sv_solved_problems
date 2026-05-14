class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        heap = []
        qua = []
        prop = []
        cost = float('inf')

        for i in range(n):
            prop.append([wage[i]/quality[i] , quality[i]])

        prop.sort()
        max_p = 0
        for i in range(n):
            p,q= prop[i]
            heapq.heappush(heap, p)
            heapq.heappush(qua, -q)
            if len(heap) == k:
                max_p = max(heap)
                cost = min(cost,(-sum(qua))*max_p)
                heapq.heappop(heap)
                heapq.heappop(qua)
        return cost






