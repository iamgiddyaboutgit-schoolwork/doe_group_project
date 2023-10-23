import networkx as nx

nx.connected_watts_strogatz_graph(
    n=1000,
    k=5,
    p=0.5
)