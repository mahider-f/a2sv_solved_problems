class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def topsort(graph,deg):
            q = deque()

            for i in range(len(deg)):
                if deg[i] == 0:
                    q.append(i)
            res = []

            while q:
                node = q.popleft()
                res.append(node)

                for neighbhour in graph[node]:
                    deg[neighbhour] -= 1
                    if deg[neighbhour] == 0:
                        q.append(neighbhour)
            if len(res) == len(deg):
                return res
            return []


        gid = m
        for i in range(n):
            if group[i] == -1:
                group[i] = gid
                gid += 1
        
        item = [[] for _ in range(n)]
        grp = [[] for _ in range(gid)]
        item_deg = [0] * n
        grp_deg = [0] * (gid)

        for i in range(n):
            for req in beforeItems[i]:
                item[req].append(i)
                item_deg[i] += 1
                if group[i] != group[req]:
                    grp[group[req]].append(group[i])
                    grp_deg[group[i]] += 1
        
        itemOrder = topsort(item, item_deg)
        groupOrder =topsort(grp, grp_deg)

        if not itemOrder or not groupOrder:
            return []

        sorted_grp = [[] for _ in range(gid)]
        for itm in itemOrder:
            sorted_grp[group[itm]].append(itm)

        result = []

        for g in groupOrder:
            result.extend(sorted_grp[g])
        return result