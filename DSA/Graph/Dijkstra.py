import heapq as hq
from collections import defaultdict

class Solution(object):

    def addEdge(self,u,v):

        self.G[u].append(v)

    
    def Dijkstra(self,s):

        self.parent[s] = -1
        self.dist[s] = 0

        Q = []

        Q.append((self.dist[s],s))

        hq.heapify(Q)

        while Q:

            (cost,u) = hq.heappop(Q)

            for v in self.G[u]:

                if(self.dist[v] == float('inf') or self.dist[v] > self.dist[u] + 1):

                    self.dist[v] = self.dist[u] + 1
                    self.parent[v] = u
                    hq.heappush(Q,(self.dist[v],v))

    


    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        self.G = defaultdict(list)

        self.ans = []

        
        self.parent = [-1 for _ in range(n)]

        for i in range(0,n-1):
            self.addEdge(i,i+1)

        for q in queries:

            self.dist = [float('inf') for _ in range(n)]

            self.addEdge(q[0],q[1])

            self.Dijkstra(0)

            self.ans.append(self.dist[n-1])

        return self.ans



        

        
