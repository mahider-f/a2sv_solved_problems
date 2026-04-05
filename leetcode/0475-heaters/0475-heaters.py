class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def check(radius):
        
            i,j = 0,0
            n,m = len(houses), len(heaters)

            while i < n:
                if j >= m:
                    return False
                l = heaters[j] - radius
                r = heaters[j] + radius

                if houses[i] < l:
                    return False
                if houses[i] > r:
                    j+=1
                else:
                    i+=1
            return True

        left, right = 0,max(abs(houses[-1]- heaters[0]), abs(heaters[-1] - houses[0]))
        while left < right:
            mid = (left + right)//2

            if check(mid):
                right = mid 
            else:
                left = mid +1
        return int(left)

                


            