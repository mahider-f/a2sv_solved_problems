class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0]*(n+1)

        for l, r in requests:
            freq[l] += 1
            if r+1 < n:
                freq[r+1] -= 1

        for i in range(1, n):
            freq[i] += freq[i-1]

        freq.pop()  

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        mod = 10**9 + 7
        ans = 0

        for i in range(n):
            ans = (ans + nums[i]*freq[i]) % mod

        return ans