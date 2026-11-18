class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            n  = len(s)
            arr = []
            for i in range(0,n,k):
                val = 0
                for j in range(i,min(i+k, n)):
                    val += int(s[j])
                arr.append(str(val))
            s = "".join(arr)
        return s
        