class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def search(capacity):
            curr = 0
            count = 1

            for x in weights:
                curr += x

                if curr > capacity:
                    count += 1
                    curr = x

                if count > days:
                    return False
            return True

        low, high = max(weights), sum(weights)

        while low <= high:
            mid = (low + high) // 2

            if search(mid):
                high = mid -1

            else:
                low = mid +1
        return low