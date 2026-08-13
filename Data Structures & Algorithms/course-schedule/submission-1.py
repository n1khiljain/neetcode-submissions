class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        indegree = [0] * numCourses
        k = 0

        for u, v in prerequisites: # v -> u
            indegree[u] += 1
            adj[v].append(u)
        
        # add those where indegree is 0
        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            course = queue.popleft()
            k += 1 #increment k if we pop

            if course in adj:
                for x in adj[course]:
                    indegree[x] -= 1
                    if indegree[x] == 0:
                        queue.append(x)
        
        return k == numCourses




        