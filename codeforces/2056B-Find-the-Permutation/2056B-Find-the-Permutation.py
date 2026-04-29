import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    g = [input().strip() for _ in range(n)]
    p = list(range(n))

    def is_better(x, y):

        if g[x][y] == '1':
            return x < y
        else:
            return x > y

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if is_better(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_p = merge_sort(p)
    print(*[x + 1 for x in sorted_p])

t_str = input().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        solve()