class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        mid = []
        larger= []

        for x in nums:
            if x<pivot:
                smaller.append(x)
            elif x>pivot:
                larger.append(x)
            else:
                mid.append(x)
        return smaller+mid+larger