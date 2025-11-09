import matplotlib.pyplot as plt
import networkx as nx
dc1= False

if dc1==True:
    from decisiontreedc1 import get_paths
else:
    from decisiontreedc2 import get_paths
paths = get_paths()
#print(paths)
G = nx.DiGraph()
edge_labels = {}
"""pos={}
options = [] #helper to determine the x offset for the tree
print(paths)
y_axis = {}
y_pos=0
for x in paths:
    for y in x:
        if y not in y_axis and y != 'result':
            y_axis[y] = y_pos
            y_pos-=2


for x in paths:
    last=''
    for y in x:
        if last != '':
            if y =='result':
                options.append({last:x[y]})
                last =''
            elif y != 'result':
                if {last:y} not in options:
                    options.append({last:y})
        last =y
done =[]

x_axis ={}
for x in options:
    key = next(iter(x))
    if key not in done:
        x_pos = 0
        offset=0
        for y in options:
            if key == next(iter(y)):
                x_axis.update({str(y):x_pos})
                offset =x_pos
                x_pos +=2
                done.append(next(iter(y)))
        offset= offset/2
        for y in options:
            if key == next(iter(y)):
                a = x_axis[str(y)]
                a-=offset
                x_axis[str(y)] = a"""


def inner_layers(y):
    subsub = ''
    #check =""
    for sub in y:
        check = sub
        if sub != 'result':
            if subsub !='':
                check = sub
                #G.add_edge(subsub, check)
                if y[subsub]in edge_labels.values() and sub in G.nodes():
                    check = check +'_1'
                G.add_edge(subsub, check)
                edge_labels[(subsub, check)] = y[subsub]

        if sub == 'result':
            check = y[sub]
            if y[subsub]in edge_labels.values():
                check = str(check)+'_1'
            G.add_edge(subsub, check)
            edge_labels[(subsub, check)] = y[subsub]


        #print("sub",sub,"subsub",subsub, edge_labels)
        check = sub
        subsub = check
    #print(pos)
    return

for x in paths:

    inner_layers(x)


levels = {}


def assign_levels(node, level=0):
    if node in levels:
        return
    levels[node] = level
    for child in G.successors(node):
        assign_levels(child, level + 1)


assign_levels('Forecast')


pos = {}
layer_nodes = {}
for node, level in levels.items():
    layer_nodes.setdefault(level, []).append(node)


for level, nodes in layer_nodes.items():
    width = len(nodes)
    for i, node in enumerate(nodes):
        pos[node] = (i - width / 2, -level)
print(pos)
# Zeichnen
#pos = nx.spring_layout(G, seed=42) # Layout
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()