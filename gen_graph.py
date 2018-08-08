#!/usr/bin/env python3
#
# Name: Dependency Graph Generator
# Author: Vincent Perricone
# License: Released under "Simplified BSD License"
# Description:
# gen_graph.py generates fancy graphs from files in serializable NetworkX json format [1].
# These json files are read from the 'dots' directory. All files in this directory need to
# have the extension '.dot.json'.
#
# To get started there are a few examples in the 'dots' directory. Familiarity with graphviz
# is pretty important too. The NetworkX documentation is pretty amazing so check it out.
#
# [1]: https://networkx.github.io/documentation/stable/reference/readwrite/json_graph.html
#
import os
import json
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph

#Directory and extension of files expected.
dots_dir = 'dots'
desired_file_extension = '.dot.json'

#Output png image filename
output_file_png = 'generated_graph.png'

# Create default generic directed graph
G = nx.DiGraph(name='Graph', strict=False, directed=True)

# Store graphs in node-link-format after being deserialized into memory
graphs = []

def output_graph(output_file='generated_graph.png'):
    """
    Save generate image to path defined by output_file parameter to disk.
    """
    nx.draw(G, with_labels=True)
    plt.savefig(output_file_png)

def build_graph():
    """
        Loop over graphs in list graphs and compose larger graph.
        We access global initial graph G for ease
    """
    global G
    for graph in graphs:
        G = nx.compose(G, graph)

def load_json_dots(search_path):
    """
        Find json files that meet extension parameters defined by
        desired_file_extension variable.
        Deserialize into memory and store in graphs list
    """
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith(desired_file_extension):
                with open(os.path.join(root, file)) as f:
                    file_data = json.load(f)
                    graph_data = json_graph.node_link_graph(file_data)
                    graphs.append(graph_data)

def main():
    load_json_dots(dots_dir)
    build_graph()
    output_graph()

if __name__== "__main__":
    main()
