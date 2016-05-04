import matplotlib.pyplot as plt
import networkx as nx
cluster1 = [(25, 1215.0, 245.0),(26, 1320.0, 315.0),(27, 1250.0, 400.0),(11, 1220.0, 580.0),(50, 1340.0, 725.0),(10, 1605.0, 620.0),(51, 1740.0, 245.0),(12, 1465.0, 200.0),(13, 1530.0, 5.0),(46, 1170.0, 65.0),(25, 1215.0, 245.0)]
cluster2 = [(15, 725.0, 370.0),(45, 830.0, 485.0),(24, 975.0, 580.0),(3, 945.0, 685.0),(42, 875.0, 920.0),(32, 1150.0, 1160.0),(9, 650.0, 1130.0),(8, 580.0, 1175.0),(7, 525.0, 1000.0),(40, 475.0, 960.0),(18, 510.0, 875.0),(44, 555.0, 815.0),(31, 575.0, 665.0),(21, 520.0, 585.0),(0, 565.0, 575.0),(48, 605.0, 625.0),(34, 685.0, 595.0),(35, 685.0, 610.0),(38, 720.0, 635.0),(39, 760.0, 650.0),(37, 795.0, 645.0),(14, 845.0, 680.0),(5, 880.0, 660.0),(4, 845.0, 655.0),(23, 835.0, 625.0),(47, 830.0, 610.0),(36, 770.0, 610.0),(33, 700.0, 580.0),(43, 700.0, 500.0),(15, 725.0, 370.0)]
cluster3 =[(49, 595.0, 360.0),(19, 560.0, 365.0),(22, 480.0, 415.0),(30, 420.0, 555.0),(17, 415.0, 635.0),(2, 345.0, 750.0),(16, 145.0, 665.0),(20, 300.0, 465.0),(41, 95.0, 260.0),(6, 25.0, 230.0),(1, 25.0, 185.0),(29, 410.0, 250.0),(28, 660.0, 180.0),(49, 595.0, 360.0)]


def draw_graph(nodes1,locs1,nodes2,locs2,nodes3,locs3):
    plt.figure(1,figsize=(15,15))
    plt.axis([-100, 1800, -50, 1300])
    # create networkx graph
    G=nx.Graph()
    G2=nx.Graph()
    G3=nx.Graph()

    # add nodes
    for n in range(0,len(locs1)-1):
        G.add_node(nodes1[n],pos=locs1[n])

    # add edges
    for e in range(0,len(nodes1)-2):
        G.add_edge(nodes1[e], nodes1[e+1])
    # draw graph

    for n in range(0,len(locs2)-1):
        G.add_node(nodes2[n],pos=locs2[n],color='#ff6666')
    # add edges
    for e in range(0,len(nodes2)-2):
        G.add_edge(nodes2[e], nodes2[e+1])
    G.add_edge(nodes1[0],nodes2[-1])


    for n in range(0,len(locs3)-1):
        G.add_node(nodes3[n],pos=locs3[n],color='#33ff99')
    # add edges
    for e in range(0,len(nodes3)-2):
        G.add_edge(nodes3[e], nodes3[e+1])
    G.add_edge(nodes1[-1],nodes2[-1])    
    G.add_edge(nodes2[-2],nodes3[-1]) 
    G.add_edge(nodes3[-2],nodes1[-2]) 
    # draw graph
    pos=nx.get_node_attributes(G,'pos')
    color=nx.get_node_attributes(G,'color')
    nx.draw_networkx_nodes(G,pos,nodelist=nodes1,node_color='#80ccff',node_size=500,with_labels=True)
    nx.draw_networkx_nodes(G,pos,nodelist=nodes2,node_color='#ff6666',node_size=500,with_labels=True)
    nx.draw_networkx_nodes(G,pos,nodelist=nodes3,node_color='#33ff99',node_size=500,with_labels=True)
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
    nx.draw_networkx_labels(G,pos,font_size=12)
    #nx.draw(G,pos,with_labels=True,node_size=500,node_color=color)

    # show graph
    plt.show()

# draw example
x = zip(*cluster1)
graph = zip(x[1],x[2])
edges = x[0]

x2 = zip(*cluster2)
graph2 = zip(x2[1],x2[2])
edges2 = x2[0]

x3 = zip(*cluster3)
graph3 = zip(x3[1],x3[2])
edges3 = x3[0]
print(edges)
draw_graph(edges,graph,edges2,graph2,edges3,graph3)
