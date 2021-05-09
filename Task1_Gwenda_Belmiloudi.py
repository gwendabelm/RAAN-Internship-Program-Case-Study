# Author: Gwenda Belmiloudi-Michel
# Date: 8th May 2021
# Title: Case Study for the internship "Computer Science or Machine Learning Students in Advanced Analytics Network" (Task 1)
# Description: Python code to plot network virtualization of network architecture
# Version: Data hard coded

## LIBRARIES

from pandas import *
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

## DATA: HARD CODING AND TRANSFORMATION IN ARRAY OR DICT

# Dictionnary of the sheet 'edges' from the xlsx file
dict_g = {'source_id': {0: 966, 1: 966, 2: 649, 3: 941, 4: 966, 5: 966, 6: 966, 7: 966, 8: 457, 9: 639, 10: 747, 11: 185, 12: 349, 13: 966, 14: 1157, 15: 966, 16: 966, 17: 966, 18: 552, 19: 966, 20: 574, 21: 966, 22: 966, 23: 966, 24: 813, 25: 792, 26: 792, 27: 966, 28: 1009, 29: 966, 30: 879, 31: 709}, 'target_id': {0: 945, 1: 879, 2: 966, 3: 966, 4: 467, 5: 1042, 6: 785, 7: 619, 8: 966, 9: 966, 10: 966, 11: 966, 12: 966, 13: 639, 14: 966, 15: 1152, 16: 517, 17: 158, 18: 966, 19: 498, 20: 966, 21: 1157, 22: 185, 23: 1025, 24: 966, 25: 966, 26: 652, 27: 172, 28: 966, 29: 3, 30: 966, 31: 966}, 'weights': {0: 13, 1: 10, 2: 9, 3: 8, 4: 8, 5: 7, 6: 7, 7: 7, 8: 7, 9: 6, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6, 15: 6, 16: 6, 17: 6, 18: 6, 19: 6, 20: 6, 21: 5, 22: 5, 23: 5, 24: 5, 25: 5, 26: 5, 27: 5, 28: 5, 29: 5, 30: 5, 31: 5}}

# Data frame created from the previous dictionnary (will be used later for the graph creation)
df = pd.DataFrame(data=dict_g)

# Dictionnary of the sheet 'nodes' from the xlsx file
dict_nodes = {'node_id': {0: 3, 1: 158, 2: 172, 3: 185, 4: 349, 5: 457, 6: 467, 7: 498, 8: 517, 9: 552, 10: 574, 11: 619, 12: 639, 13: 649, 14: 652, 15: 709, 16: 747, 17: 785, 18: 792, 19: 813, 20: 879, 21: 941, 22: 945, 23: 966, 24: 1009, 25: 1025, 26:1042, 27: 1152, 28: 1157}, 'node_color': {0: '#0066CC', 1: '#0066CC', 2: '#0066CC', 3: '#0066CC', 4: '#0066CC', 5: '#A05EB5', 6: '#A05EB5', 7: '#A05EB5', 8: '#A05EB5', 9: '#A05EB5', 10: '#00965E', 11: '#00965E', 12: '#00965E', 13: '#00965E', 14: '#00965E', 15: '#E40046', 16: '#E40046', 17: '#E40046', 18: '#E40046', 19: '#E40046', 20: '#ED8B00', 21: '#ED8B00', 22: '#ED8B00', 23: '#ED8B00', 24: '#ED8B00', 25: '#B1B3B3', 26: '#B1B3B3', 27: '#B1B3B3', 28: '#B1B3B3'}, 'node_label': {0: 'James', 1: 'John', 2: 'Robert', 3: 'Michael', 4: 'William', 5: 'David',
6: 'Richard', 7: 'Joseph', 8: 'Thomas', 9: 'Charles', 10: 'Mary', 11: 'Patricia', 12: 'Jennifer', 13: 'Linda', 14: 'Elizabeth', 15: 'Barbara', 16: 'Susan', 17: 'Jessica', 18: 'Sarah', 19: 'Karen', 20: 'Christopher', 21: 'Daniel', 22: 'Matthew', 23: 'Anthony', 24: 'Nancy', 25: 'Lisa', 26: 'Margaret', 27: 'Betty', 28: 'Sandra'}}

# Array of the sheet 'nodes' from the xlsx file
array_nodes = np.array([[3, '#0066CC', 'James'], [158, '#0066CC', 'John'], [172, '#0066CC', 'Robert'], [185, '#0066CC', 'Michael'], [349, '#0066CC', 'William'],[457, '#A05EB5', 'David'],[467, '#A05EB5', 'Richard'],[498, '#A05EB5', 'Joseph'],[517, '#A05EB5', 'Thomas'],[552, '#A05EB5', 'Charles'],[574, '#00965E', 'Mary'],[619, '#00965E', 'Patricia'],[639, '#00965E', 'Jennifer'],[649, '#00965E', 'Linda'],[652, '#00965E', 'Elizabeth'],[709, '#E40046', 'Barbara'],[747, '#E40046', 'Susan'],[785, '#E40046', 'Jessica'],[792, '#E40046', 'Sarah'],[813, '#E40046', 'Karen'],[879, '#ED8B00', 'Christopher'],[941, '#ED8B00', 'Daniel'],[945, '#ED8B00', 'Matthew'],[966, '#ED8B00', 'Anthony'],[1009, '#ED8B00', 'Nancy'],[1025, '#B1B3B3', 'Lisa'],[1042, '#B1B3B3', 'Margaret'],[1152, '#B1B3B3', 'Betty'],[1157, '#B1B3B3', 'Sandra']], dtype = object)

# Creation of dictionnary with nodes labels as values and nodes id as key
dict_nodeId_label = {}
for i in range(0,len(array_nodes)):
    key = array_nodes[i,0]
    value = array_nodes[i,2]
    dict_nodeId_label [key] = value

## PLOT OF NETWORK IN 2D

# Graph creation
g = nx.from_pandas_edgelist(df, source = 'source_id', target = 'target_id', edge_attr = 'weights')


fig, axs = plt.subplots()

# List of nodes id
list_nodes = list(g)
list_nodes.sort()

# Position of nodes in 2D
pos=nx.spring_layout(g)

# Draw the 2D network
nx.draw_networkx(g, pos = pos, with_labels = False, nodelist = list_nodes, node_color = array_nodes[0:len(array_nodes),1], ax = axs)

nx.draw_networkx_labels (g, pos=pos, labels = {n:lab for n,lab in dict_nodeId_label.items() if n in pos})

axs.set_title('Network Visualization 2D')

plt.show()

## PLOT OF NETWORK IN 3D

# Position of nodes in 3D
pos3D = nx.spring_layout(g,dim=3)
pos3D = dict(sorted(pos3D.items()))
pos3D_list = list(pos3D.values())

# Nodes coordinates separation
x_nodes = [pos3D_list[i][0] for i in range(len(list_nodes))]
y_nodes = [pos3D_list[i][1] for i in range(len(list_nodes))]
z_nodes = [pos3D_list[i][2] for i in range(len(list_nodes))]

# Creation of edges list in 3D
edge_list = g.edges()

x_edges=[]
y_edges=[]
z_edges=[]


for edge in edge_list:
    x_edges += [pos3D[edge[0]][0],pos3D[edge[1]][0],None]

    y_edges += [pos3D[edge[0]][1],pos3D[edge[1]][1],None]

    z_edges += [pos3D[edge[0]][2],pos3D[edge[1]][2],None]


# Draw the 3D network

# First the edges
trace_edges = go.Scatter3d(x=x_edges,
                        y=y_edges,
                        z=z_edges,
                        mode='lines',
                        line=dict(color='black', width=2),
                        hoverinfo='none')

# Then the nodes
trace_nodes = go.Scatter3d(x=x_nodes,
                         y=y_nodes,
                        z=z_nodes,
                        text=array_nodes[0:len(array_nodes),2],
                        mode='markers',
                        marker=dict(symbol='circle',
                                    size=10,
                                    color=array_nodes[0:len(array_nodes),1],
                                    line=dict(color='black', width=0.5)),
                        hoverinfo='text')

# And finally the axis and layout for the plot
axis = dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title='')

layout = go.Layout(title="Network Visualization 3D",
                width=650,
                height=625,
                showlegend=False,
                scene=dict(xaxis=dict(axis),
                        yaxis=dict(axis),
                        zaxis=dict(axis),
                        ),
                margin=dict(t=100),
                hovermode='closest')

traces = [trace_edges, trace_nodes]
fig = go.Figure(data=traces, layout=layout)

fig.show()
