class Solution:
    def checkString(self, s: str) -> bool:
        total = s.count('a')
        countA = 0
        
        if total == len(s):
            return True

        for x in s:
            if x == "a":
                countA+=1
            else:
                return(countA == total)
