class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        if len(merged) %2 == 1:
            mid = len(merged)//2
            return merged[mid]

        l, r = 0, len(merged) - 1
        mid = (l+r)//2
        return (merged[mid] + merged[mid+1]) /2

            