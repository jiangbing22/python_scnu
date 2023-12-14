import networkx as nx
import matplotlib.pyplot as plt
import csv

plt.rcParams["font.sans-serif"] = [u"SimHei"]
plt.rcParams["axes.unicode_minus"] = False
G = nx.DiGraph()
with open('triples.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    datas = [line for line in reader]
    del datas[0]

nodes = list({data[0] for data in datas}.union({data[1] for data in datas}))

G.add_nodes_from(nodes)
for data in datas:
    G.add_edge(data[0], data[1], relation=data[3])
plt.figure(figsize=(38,16),dpi=200)
pos = nx.spring_layout(G,k=0.3)
nx.draw(G, pos, with_labels=True, font_size=10, node_size=200, font_color="black", node_color="lightgreen", edge_color="black")
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red",clip_on=False)
plt.show()
