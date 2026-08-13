class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        indegree = [0] * numCourses
        res = []

        for u, v in prerequisites: # v -> u
            indegree[u] += 1
            adj[v].append(u)
        
        # add those where indegree is 0
        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            course = queue.popleft()
            res.append(course)

            if course in adj:
                for x in adj[course]:
                    indegree[x] -= 1
                    if indegree[x] == 0:
                        queue.append(x)
        
        return res if len(res) == numCourses else []