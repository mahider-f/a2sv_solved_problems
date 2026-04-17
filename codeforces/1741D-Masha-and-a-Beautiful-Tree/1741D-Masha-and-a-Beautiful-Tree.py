def mergeSort(l,r):
        global count, possible

        if r -l == 1:
            return tree[l], tree[l]
        
        mid = (l+r) // 2

        left_min, left_max = mergeSort(l, mid)
        right_min, right_max = mergeSort(mid, r)

        if not possible:
            return 0,0
        
        if left_max < right_min:
            return left_min, right_max
        
        elif right_max < left_min:
            count += 1
            return right_min, left_max
        else:
            possible = False
            return 0,0
    mergeSort(0,len(tree))

    print(count if possible else -1)