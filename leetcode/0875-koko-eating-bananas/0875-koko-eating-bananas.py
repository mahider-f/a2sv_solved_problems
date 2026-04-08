class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            hours = 0

            for banana in piles:
                hours += ceil(banana/mid)
            return hours <= h

        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r) // 2

            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        