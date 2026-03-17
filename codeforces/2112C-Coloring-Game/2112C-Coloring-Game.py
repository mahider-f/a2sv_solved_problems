t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    max_ = arr[-1]

    for i in range(n-1, 1, -1):
        left = 0
        for j in range(i-1, 0, -1):
            while (arr[left] + arr[j] <= arr[i] and left < j) or (arr[i] + arr[left] + arr[j] <= max_ and left < j):
                left += 1

            if j == left: 
                break
            count+= j - left

            
    print(count)