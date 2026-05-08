class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums = []
        res = []

        for i in range(len(nums1)):
            heapq.heappush(nums,(nums1[i]+ nums2[0], [nums1[i],nums2[0]], (i, 0)))
        for _ in range(k):
            su, a, inds = heapq.heappop(nums)
            res.append(a) 
            i, j = inds 
            if j+1 < len(nums2):
                j+=1
                heapq.heappush(nums,(nums1[i]+ nums2[j], [nums1[i],nums2[j]], (i, j)))    

        return res