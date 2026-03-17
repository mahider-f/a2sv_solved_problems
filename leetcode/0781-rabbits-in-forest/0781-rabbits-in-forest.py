class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0

        for x in count:
            a = count[x] // (x+1)
            b = count[x] / (x+1)
            if x == 0:
                ans += count[x]
            elif x != 0 and count[x] <= (x+1):
                ans += (x+1)
            elif x != 0 and a < b:
                ans += ((a+1)*(x+1))
            elif x != 0 and a == b:
                ans += (a*(x+1))

            
        return ans

        