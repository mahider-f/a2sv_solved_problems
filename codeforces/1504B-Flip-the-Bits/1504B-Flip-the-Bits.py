t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    balance = [0] * n
    cur = 0

    for i in range(n):
        if a[i] == '1':
            cur += 1
        else:
            cur -= 1
        balance[i] = cur

    flipped = False
    possible = True


    for i in range(n - 1, -1, -1):
        
        current_bit = a[i]
        
        if flipped:
            current_bit = '1' if current_bit == '0' else '0'

        if current_bit != b[i]:
            if balance[i] == 0:
                flipped = not flipped
            else:
                possible = False
                break

    print("YES" if possible else "NO")