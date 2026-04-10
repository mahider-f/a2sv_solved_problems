class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(mid):
            inPlace = 1
            prev = position[0]

            for i in range(1, len(position)):
                cur = position[i]

                if cur - prev >= mid:
                    inPlace +=1
                    prev = cur
                
                if inPlace == m:
                    return True
            return False


        
        left, right = 0, ceil(position[-1]/(m-1))
        while left <= right:
            mid = (left + right)//2 
            if check(mid):
                left = mid + 1
            else:
                right = mid -1
        return left - 1