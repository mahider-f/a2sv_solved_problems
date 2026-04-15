class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        
        k = len(nums) - k
        l, r = 0, len(nums) - 1

        while l <= r:
            pivot = nums[random.randint(l, r)]

            
            left, i, right = l, l, r

            while i <= right:
                if nums[i] < pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
                else:
                    i += 1

            if k < left:
                r = left - 1
            elif k > right:
                l = right + 1
            else:
                return nums[k]