def get_sum(p, r1, c1, r2, c2):
    return p[r2][c2] - p[r1-1][c2] - p[r2][c1-1] + p[r1-1][c1-1]

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    h_count = get_sum(ph, r1, c1+1, r2, c2) if c1 < c2 else 0

    v_count = get_sum(pv, r1+1, c1, r2, c2) if r1 < r2 else 0

    print(h_count + v_count)