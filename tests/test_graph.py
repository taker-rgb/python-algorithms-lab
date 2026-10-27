from src.graph import Graph

def test_add_edge():
    g = Graph()
    g.add_edge(1, 2)
    assert g.adj[1] == [2]
    assert g.adj[2] == [1]
