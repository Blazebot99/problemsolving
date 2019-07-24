#An alternate adaptaion of DFS
#Takes a directed acyclic graph to make a linear ordering of its vertices so that if graph G contains edge (v, w) then vertex v comes before the vertex w in ordering. 

#Algorithm:
#1. Call dfs(g) for some graph g. DFS is used here to compute the finish times for each of the vertices.
#2. Store vertices in a list in decreasing order of finish time. 
#3. Return ordered list as result of the topological sort.