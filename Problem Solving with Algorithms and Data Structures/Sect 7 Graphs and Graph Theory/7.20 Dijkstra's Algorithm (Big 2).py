#Dijkstra's Algorithm is an iterative algorithm used to calculate the shortest path from one node to another.
#Makes use of the dist instance in the vertex class to keep track of weightings. 
#Iterates once for every vertex in the graph, but the order for iteration is determined by a priority queue.
#The priority queue stores key-value tuples instead of single values in order to ensure the matching of keys between the queue and vertex. The value is also used for deciding priority, since the vertex to be explored will always be the one with the shortest weight as we are looking to find the shortest possible path.
#decreaseKey method is also added
#Used when distance to a vertex already in the queue is reduced, moving the vertex closer to the front of the queue.

from pythonds.graphs import PriorityQueue, Graph, Vertex
def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)