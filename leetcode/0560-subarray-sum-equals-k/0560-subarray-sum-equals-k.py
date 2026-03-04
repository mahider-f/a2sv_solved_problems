class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0] = 1
        curr_sum = 0
        ans = 0
        
        for num in nums:
            curr_sum += num
            
            ans += count[curr_sum - k]
            
            count[curr_sum] += 1
            
        return ans

        
        