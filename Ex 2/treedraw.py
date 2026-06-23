from os import path

import matplotlib.pyplot as plt
import networkx as nx
dc1= False

if dc1==True:
    from decisiontreedc1 import get_paths
else:
    from decisiontreedc2 import get_paths
paths = get_paths()
print("paths",paths)
G = nx.DiGraph()
edge_labels = {}
"""data = []
nodes_leafs =[]
for x in paths:
    z=''
    for y in x:
        if z!='' and [z,y] not in data:
            if y=='result':
                data.append([z, x[y]]) #finds leafs
                if x[y] not in nodes_leafs:
                    nodes_leafs.append(x[y])
            elif y!='result':
                data.append([z,y]) #finds paths
        if [y, x[y]] not in data and y!='result': #find nodes
            data.append([y, x[y]])
            if y not in nodes_leafs:
                nodes_leafs.append(y)
        z= x[y]
i=0
label_ids = []
for x in nodes_leafs:
    for y in data:
        if y[0] == x:
            for z in data:
                if y[1] == z[0]:
                    print(y[0],z[0],z[1])
                    G.add_edge(i, i+1)
                    label_ids.append([y[0],i])
                    label_ids.append([z[1],i+1])
                    edge_labels[(i, i+1)] = z[0]
                    i+=2

                    #a = str(z[1])+str(i)
                    G.add_edge(y[0], z[1])
                    edge_labels[(y[0], z[1])] = z[0]



print(data)
print(nodes_leafs)
#options =[]"""
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

"""
"""possible_paths=[]
for x in paths:
    last=''
    for y in x:
        if last != '':
            if y =='result':
                options.append({last:x[y]})
                for z in y:
                    if {last:x[y]} in 
                last =''
            elif y != 'result':
                if {last:y} not in options:
                    options.append({last:y})
        last =y
print(options)"""
"""print(options)
def tree_draw(x,i):
    for y in x:
        print(y)
        G.add_edge(y,i)
        i+=1
for x in options:
    i=0
    tree_draw(x,i)"""
"""for x in options:
    i =0
    for y in x:
        a = y + str(i)
        b= str(x[y]) + str(i)
        G.add_edge(a,b)"""



"""
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
                x_axis[str(y)] = a

print(x_axis)"""


def inner_layers(y):
    subsub = ''

    for sub in y:
        if sub != 'result':
            if subsub !='':
                G.add_edge(subsub, sub)
                #print(subsub, "subsub", sub, "edge", y[subsub])
               #(G.edges())
                edge_labels[(subsub, sub)] = y[subsub]

        if sub == 'result':

            #if y[subsub] not in edge_labels.values():
            G.add_edge(subsub, y[sub])
            edge_labels[(subsub, y[sub])] = y[subsub]


        #print("sub",sub,"subsub",subsub, edge_labels)
        subsub = sub
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
# Zeichnen 
#pos = nx.spring_layout(G, seed=42) # Layout
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()