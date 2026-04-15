class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
         
        def backtrack(start,path):
            if start == len(num):
                return len(path) >= 3
            for i in range(start,len(num)):
                cur = num[start:i+1]

                if len(path) >= 2:
                    if int(cur) > path[-1]+path[-2]:
                        break
                    if int(cur) < path[-1]+path[-2]:
                        continue
                if cur.startswith('0') and len(cur) >1:
                    break
                if backtrack(i+1,path + [int(cur)]):
                    return True
            return False
        return backtrack(0,[])
                