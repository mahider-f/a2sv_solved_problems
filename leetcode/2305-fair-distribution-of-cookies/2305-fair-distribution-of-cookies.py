class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        self.minUnfairness = float('inf')
    
        def backtrack(i, bucket):
            if i >= len(cookies):
                self.minUnfairness = min(self.minUnfairness, max(bucket))
                return
            
            for j in range(k):
                bucket[j] += cookies[i]
                backtrack(i+1, bucket)
                bucket[j] -= cookies[i]
                if bucket[j] == 0:
                    break
    
        backtrack(0, bucket)
        return self.minUnfairness