class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        total_subarrays = 0
        current_sum = 0
        
        # Track counts of prefix sums seen so far
        even_prefix_count = 1  # Starts at 1 for an empty prefix (sum = 0)
        odd_prefix_count = 0

        for num in arr:
            current_sum += num
            
            # If current prefix sum is odd, pair it with previous even prefix sums
            if current_sum % 2 != 0:
                total_subarrays += even_prefix_count
                odd_prefix_count += 1
            # If current prefix sum is even, pair it with previous odd prefix sums
            else:
                total_subarrays += odd_prefix_count
                even_prefix_count += 1

        return total_subarrays % MOD
