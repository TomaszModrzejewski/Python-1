import math


class Graph:
    def __init__(self, N=0):  # a graph with Node 0,1,...,N-1
        self.N = N
        self.W = [[math.inf for _ in range(N)] for _ in range(N)]
        self.dp = [[math.inf for _ in range(N)] for _ in range(N)]

    def addEdge(self, u, v, w):
        self.dp[u][v] = w

    def floyd_warshall(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.dp[i][j] = min(self.dp[i][j], self.dp[i][k] + self.dp[k][j])

    def showMin(self, u, v):
        return self.dp[u][v]


if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0, 2, 9)
    graph.addEdge(0, 4, 10)
    graph.addEdge(1, 3, 5)
    graph.addEdge(2, 3, 7)
    graph.addEdge(3, 0, 10)
    graph.addEdge(3, 1, 2)
    graph.addEdge(3, 2, 1)
    graph.addEdge(3, 4, 6)
    graph.addEdge(4, 1, 3)
    graph.addEdge(4, 2, 4)
    graph.addEdge(4, 3, 9)
    graph.floyd_warshall()
    graph.showMin(1, 4)
    graph.showMin(0, 3)
