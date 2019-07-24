#Knight's tour wanted to make the deepest tree without any branching
#Generally, you want to make the most complete tree possible by searching as deeply as possible
#Depth First Forests are created when more than one tree is created
#Two new modifications will be made to Vertex class
#The addition of discovery and finish times: discovery tracks the number of steps before a vertex is encountered, finish time is the number of steps in the algorithm before a vertex becomes black (completely explored)

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
                
    #dfsvisit method begins with a single vertex (startvertex) and explores all neighboring white vertices, each one as deeply as possible
    #dfsvisit is almost identical to bfs except in that the last line of the for loop is a recursive call rather than bfs adds the node to another queue to cycle to again. 
    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
        
#Note: The start and finish times of each node have a property known as the "parenthesis property". All the children of a node in the depth first tree have a later discovery time and earlier finish time than their parent. 