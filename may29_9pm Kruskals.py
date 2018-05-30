# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:43:27 2018

@author: nidhi
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:15:29 2018

@author: nidhi
"""

# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
 
from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
    def __init__(self,graph_dic = {}):  
        self.graph_dic = graph_dic # default dictionary to store graph
        
    def vertices (self):
        vertices = list(self.graph_dic.keys())  
          # gives number of vertices 
        return vertices   
               
    # function to create list of nodes and weights(graph)
    def remove_duplicates(self, list):
        x = []
        for item in list:
            if item not in x:
                x.append(item)
        return x
    def generate_edges_weight_list(self):
        graph = []
        for u in self.graph_dic:
            #print('self.graph_dic', self.graph_dic)
            #print('u', u)
            for v in self.graph_dic[u]:
                #print('self.graph_dic[u]', self.graph_dic[u])
                #print('v', v)
                for t in range(self.graph_dic[u][v]):
                    #print('self.graph_dic[u][v]', self.graph_dic[u][v])
                    #print('t', t)
                    w = self.graph_dic[u][v]
                    #print('w', w)
                    edge_weight = [u,v,w]
                    #print ('edge_weight', edge_weight)
                    graph.append(edge_weight)
        #print('graph', graph)
        graph = self.remove_duplicates(graph)
        print ('graph_', graph)
                    
        return graph    
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root 
        # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's 
        # algorithm
    def KruskalMST(self):
 
        result =[] #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
            # Step 1:  Sort all the edges in non-decreasing 
                # order of their
                # weight.  If we are not allowed to change the 
                # given graph, we can create a copy of graph
        
        graph_ = self.generate_edges_weight_list()
        graph_ =  sorted(graph_,key=lambda item: item[2])
        print ('sorted graph in the increasing order of weight', graph_)
 
        parent = [] ; rank = []
        
        vertices = self.vertices()
        print ('vertices', vertices)
        V = len(vertices)
        print('V', V)
 
        # Create V subsets with single elements
        for node in range(V):
            parent.append(node)
            rank.append(0)
     
        # Number of edges to be taken is equal to V-1
        while e < V -1 :
 
            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration
            u,v,w =  graph_[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
 
            # If including this edge does't cause cycle, 
                        # include it in result and increment the index
                        # of result for next edge
            if x != y:
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, x, y)            
            # Else discard the edge
        print ('result', result)
        outdict = defaultdict(dict)
        for u, v, w in result:
            outdict[u][v] = w
        print('outdict',  outdict)
        # print the contents of result[] to display the built MST
        print ("Following are the edges in the constructed MST")
        for u,v,weight  in result:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d -- %d == %d" % (u,v,weight))
 
# Driver code
g = Graph({0: {1: 10, 2: 6, 3: 5}, 1: {3: 15}, 2: {3: 4}})
g.KruskalMST()

 

#This code is contributed by Neelam Yadav