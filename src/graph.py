class Graph:
    def __init__(self):
        self.adj = {}
        
    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start):
        visited, queue = set([start]), [start]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return res
