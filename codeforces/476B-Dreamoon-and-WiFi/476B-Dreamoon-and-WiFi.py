def dfs(i, position):
    global ways, total
    
    if i == len(s2):
        total += 1
        if position == target:
            ways += 1
        return
    
    if s2[i] == '+':
        dfs(i + 1, position + 1)
    elif s2[i] == '-':
        dfs(i + 1, position - 1)
    else:  
        dfs(i + 1, position + 1)
        dfs(i + 1, position - 1)

dfs(0, 0)

print(ways / total)