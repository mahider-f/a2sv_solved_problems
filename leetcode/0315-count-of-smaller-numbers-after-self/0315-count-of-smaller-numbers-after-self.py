class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = list(enumerate(nums))
        ans = [0] * len(nums)

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            i, j = 0, 0
            res = []
            count = 0

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    ans[left[i][0]] += count
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    count += 1
                    j += 1

            while i < len(left):
                ans[left[i][0]] += count
                res.append(left[i])
                i += 1

            while j < len(right):
                res.append(right[j])
                j += 1

            return res

        mergeSort(arr)
        return ans