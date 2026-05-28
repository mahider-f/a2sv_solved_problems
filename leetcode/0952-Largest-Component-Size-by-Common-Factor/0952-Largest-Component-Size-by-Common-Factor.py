class Solution:

    def find(self, x):

        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, a, b):

        pa = self.find(a)
        pb = self.find(b)

        if pa != pb:
            self.p[pa] = pb

    def largestComponentSize(self, nums: List[int]) -> int:

        self.p = list(range(max(nums) + 1))

        for v in nums:

            i = 2

            while i * i <= v:

                if v % i == 0:

                    self.union(v, i)
                    self.union(v, v // i)

                i += 1

        return max(Counter(self.find(v) for v in nums).values())