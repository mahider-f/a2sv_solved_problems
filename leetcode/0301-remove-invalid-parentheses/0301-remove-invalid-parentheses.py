class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def valid(path):
            count = 0

            for x in path:
                if x == '(':
                    count +=1
                elif x ==')':
                    count -=1
                if count < 0:
                    return False
            return count == 0

        ans = []
        q = deque()
        visited = set()
        found = False

        q.append(s)
        visited.add(s)

        while q:
            cur = q.popleft()

            if valid(cur):
                ans.append(cur)
                found = True
            
            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in ('(', ')'):
                    continue
                else:
                    string = cur[:i] + cur[i+1:]
                
                if string not in visited:
                    q.append(string)
                    visited.add(string)
        return ans


        
