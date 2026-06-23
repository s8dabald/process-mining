import matplotlib.pyplot as plt
import networkx as nx

dc1 = False
if dc1:
    from decisiontreedc1 import get_paths
else:
    from decisiontreedc2 import get_paths

paths = get_paths()
G = nx.DiGraph()
edge_labels = {}
node_counter = 0  # eindeutige interne Node-ID

for path in paths:
    parent = 'Forecast'
    if not G.has_node(parent):
        G.add_node(parent, label='Forecast')

    # Jede Node-Kombination in diesem Pfad Schritt für Schritt
    for i, (key, value) in enumerate(path.items()):
        if key == 'Forecast':
            continue

        if key == 'result':
            # Leaf-Node
            node_counter += 1
            leaf_label = f"{value}_{node_counter}"
            G.add_node(leaf_label, label=str(value))
            G.add_edge(parent, leaf_label)
            # Edge-Label ist der vorherige Key-Value
            prev_key = list(path.keys())[i-1]
            edge_labels[(parent, leaf_label)] = path[prev_key]
            parent = leaf_label
            continue

        # Intermediate Node
        child_label = str(value) + f"_{node_counter+1}"  # eindeutiger Node-Name
        node_counter += 1
        G.add_node(child_label, label=key)
        G.add_edge(parent, child_label)
        # Edge-Label = Value der Variable
        edge_labels[(parent, child_label)] = value
        parent = child_label

# Levels berechnen
levels = {}
def assign_levels(node, level=0):
    if node in levels:
        return
    levels[node] = level
    for child in G.successors(node):
        assign_levels(child, level + 1)

assign_levels('Forecast')

# Positionen pro Ebene
pos = {}
layer_nodes = {}
for node, level in levels.items():
    layer_nodes.setdefault(level, []).append(node)

for level, nodes in layer_nodes.items():
    width = len(nodes)
    for i, node in enumerate(nodes):
        pos[node] = (i - width / 2, -level)

# Node-Labels aus Attributen
node_labels = {n: G.nodes[n]['label'] for n in G.nodes}

# Zeichnen
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=2000, node_color='lightblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.show()
