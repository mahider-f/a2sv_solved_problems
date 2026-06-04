class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # S = set(s)
        # T = set(t)
        # a =  list(T.difference(S))
        # return "".join(a)
        S = Counter(s)
        T = Counter(t)
        a = []

        for x in t:
            if T[x] > S[x]:
                a.append(x)
        a = set(a)
        return "".join(a)