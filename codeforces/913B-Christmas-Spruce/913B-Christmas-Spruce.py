n = int(input())

children = [[] for _ in range(n+1)]

for i in range(2,n+1):
    parent = int(input())
    children[parent].append(i)

for node in range(1,n+1):
    if len(children[node]) > 0:
        leaf = 0

        for child in children[node]:
            if len(children[child]) == 0:
                leaf +=1
    if leaf < 3:
        print('No')
        exit()

print('Yes')