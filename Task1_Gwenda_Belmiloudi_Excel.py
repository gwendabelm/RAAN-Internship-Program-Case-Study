# Author: Gwenda Belmiloudi-Michel
# Date: 8th May 2021
# Title: Case Study for the internship "Computer Science or Machine Learning Students in Advanced Analytics Network" (Task 1)
# Description: Python code to plot network virtualization of network architecture
# Version: Data from the xlsx file

## LIBRARIES

from pandas import *
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

## DATA: RETRIEVE FROM THE XLSX FILE

# Replace the value of file_location by your own path
file_location = r"C:\Users\gwend\Documents\CV et stage\3A\Roche\Computer Science or Machine Learning\Case study\raan_case_study_interns.xlsx"

# Read the excel file
xls = ExcelFile(file_location)

# Transformation of excel sheets in dataframe, dictionnary or array
df = xls.parse(xls.sheet_names[0])
dict_g = df.to_dict()

df_nodes = xls.parse(xls.sheet_names[1])
dict_nodes = df_nodes.to_dict()

array_nodes = df_nodes.to_numpy()

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
list_nodes_id = list(g)
list_nodes_id.sort()

# Position of nodes in 2D
pos=nx.spring_layout(g)

# Draw the 2D network
nx.draw_networkx(g, pos = pos, with_labels = False, nodelist = list_nodes_id, node_color = array_nodes[0:len(array_nodes),1], ax = axs)
nx.draw_networkx_labels (g, pos=pos, labels = {n:lab for n,lab in dict_nodeId_label.items() if n in pos})

axs.set_title('Network Visualization 2D')
plt.show()

## PLOT OF NETWORK IN 3D

# Position of nodes in 3D
pos3D = nx.spring_layout(g,dim=3)
pos3D = dict(sorted(pos3D.items()))
pos3D_list = list(pos3D.values())

# Nodes coordinates separation
x_nodes = [pos3D_list[i][0] for i in range(len(list_nodes_id))]
y_nodes = [pos3D_list[i][1] for i in range(len(list_nodes_id))]
z_nodes = [pos3D_list[i][2] for i in range(len(list_nodes_id))]

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

data = [trace_edges, trace_nodes]
fig = go.Figure(data=data, layout=layout)

fig.show()
