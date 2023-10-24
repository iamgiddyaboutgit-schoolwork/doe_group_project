#!/usr/bin/env python3

from pathlib import Path

import networkx as nx
from pyvis.network import Network

PARENT_PATH = Path(__file__).resolve().parents[1]

def main():
    create_world()




def create_world():
    world = Network(
        neighborhood_highlight=True, 
        select_menu=True, 
        filter_menu=True
    )

    pre_world = nx.connected_watts_strogatz_graph(
        n=100,
        k=5,
        p=0.5
    )

    # pre_world = nx.scale_free_graph(
    #     n=100,
    #     alpha=0.1,
    #     beta=0.7,
    #     gamma=0.2,
    # )

    world.from_nx(nx_graph=pre_world)
    world.show("world.html")





if __name__ == "__main__":
    main()