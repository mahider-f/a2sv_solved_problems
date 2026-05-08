class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        res = []

        for i in count.keys():
            heapq.heappush(heap, (-count[i], i))

            # if len(heap) > k:
            #     heapq.heappop(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res