class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        # n = len(instructions)
        # inst = sorted(instructions)
        # nums = instructions
        # cost = 0
        # cnt = 0
        
        # small = []
        # large = [0]*n
        # stack1 = []
        # stack2 = []
        mod = (10**9 +7)
        # for x in instructions:
        #     while stack1 and x <= stack1[-1]:
        #         stack1.pop()
        #     small.append(len(stack1))
        #     stack1.append(x)
        # for x in inst:
        #     i = instructions.index(x)
        #     j = nums.index(x)
        #     cnt += len(nums[:j])
        #     large[i] = cnt
        #     nums.pop(j)
        # for i in range(n):
        #     cost += min(small[i],large[i])
        # print(small)
        # print(large)
        # print(instructions)

        cost = 0
        nums = []

        for x in instructions:
            smaller = bisect_left(nums, x)
            greater = len(nums) - bisect_right(nums, x)
            cost += min(smaller, greater)
            insort(nums, x)
        return cost % mod