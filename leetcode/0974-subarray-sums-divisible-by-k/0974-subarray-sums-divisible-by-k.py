class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0] = 1
        curr_sum = 0
        ans = 0
        
        for num in nums:
            curr_sum += num
            
            ans += count[curr_sum % k]
            
            count[curr_sum % k] += 1
            
        return ans
        