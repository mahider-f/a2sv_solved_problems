class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avialable = []
        pending = []
        time = 0
        res = []
        for i, (enqueueTime, processTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processTime, i))
        
        while pending or avialable:
            while pending and pending[0][0] <= time:
                wt,pt,i = heapq.heappop(pending)
                heapq.heappush(avialable,(pt,i))

            if not avialable:
                time = pending[0][0]
                continue
            
            pt, i = heapq.heappop(avialable)
            time += pt
            res.append(i)
        return res