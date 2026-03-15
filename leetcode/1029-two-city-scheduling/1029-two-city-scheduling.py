class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff = {}
        a, b = n//2, n//2
        idx = 0
        ans = 0

        for x in costs:
            diff[idx] = abs(x[0] - x[1])
            idx += 1
        
        diff = dict(sorted(diff.items(), key=lambda a: a[1], reverse=True))

        for i in diff:             
            if costs[i][1] <= costs[i][0] and a > 0 and b > 0: 
                ans += costs[i][1]
                b -= 1

            elif costs[i][0] < costs[i][1] and a > 0 and b > 0:
                ans += costs[i][0]
                a -= 1

            elif a <= 0 and b > 0:
                ans += costs[i][1]
                b -= 1

            elif b <= 0 and a > 0:
                ans += costs[i][0]
                a -= 1

        return ans