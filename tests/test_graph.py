from src.graph import Graph

def test_add_edge():
    g = Graph()
    g.add_edge(1, 2)
    assert g.adj[1] == [2]
    assert g.adj[2] == [1]

def test_bfs():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    assert set(g.bfs(1)) == {1, 2, 3}
