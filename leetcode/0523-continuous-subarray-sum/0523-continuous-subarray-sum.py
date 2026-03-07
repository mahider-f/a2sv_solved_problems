class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = Counter()
        count[0] = -1
        curr_sum = 0
        ans = 0

        for i, num in enumerate(nums):
            curr_sum += num
            r = curr_sum % k
            
            if r in count:
                if i - count[r] > 1:
                    return True
            else:
                count[r] = i
            
        return False
        
        