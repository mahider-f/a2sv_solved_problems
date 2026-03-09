class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        stack = []
        for v in nums2:
            while stack and stack[-1] < v:
                m[stack.pop()] = v
            stack.append(v)
        return [m.get(v, -1) for v in nums1]