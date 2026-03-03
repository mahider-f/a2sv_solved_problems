t = int(input())

for _ in range(t):
    r = int(input())
    red = list(map(int,input().split()))
    b = int(input())
    blue = list(map(int,input().split()))

    one = [0]*(r+1)
    two = [0]*(b+1)

    for i in range(1,r+1):
        one[i] = one[i-1] + red[i-1]
    for i in range(1,b+1):
        two[i] = two[i-1] + blue[i-1]
    print(max(one)+max(two))