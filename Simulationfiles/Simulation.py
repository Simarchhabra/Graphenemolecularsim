class Simulation():
        
    global Grid;
    Grid = []; #Initializes a list called Grid that becomes a model of Graphene's molecular structure 
    
    def make_grid(self, n): #creates the 2-d grid with parameter n to indicate amount of nodes in grid
        
        def nodeobject(node): #creates nodeobject that represents carbon atom in Graphene structure
            self.node = node;
            
        self.n = n;
        
        for i in range(n):
            Additive=[] #creates temporary list to store Nodeobject
            
            for j in range(n):
                
                NewNode=Node()
                Additive.append(NewNode)
                
            Grid.append(Additive); #uses additive to create 2d grid with Nodeobjects from Nodeclass
        
        return True;
        
    def populateNeighbors(self): #iterates over node objects to define its neighbors
    
        c1=0; #counter variable 1
        c2=0; #counter variable 2
        
        gridsize=len(Grid) #Finds size of grid
        gridwithinsize=len(Grid[0]) #Finds size of lists of Node objects within grid
        
        for list01 in Grid:
            
            for Node1 in list01:
                
                Neighborlist=[] #List of neighbors of node
                
                if ((c1>0)and(c1<gridsize)and(c2>0)and(c2<gridwithinsize)): #Find neighbors of nodes not on the edges/corners of the grid
                
                    Neighborlist.append(Grid[c1][c2+1]) #Add the node to the right of the current node to the list of neighbors
                    Neighborlist.append(Grid[c1][c2-1]) #Add the node to the left of the current node to the list of neighbors
                    
                    if (c1%2!=0): #If the row number of the current node is not even, add the node above the current node to the list of neighbors
                        Neighborlist.append(Grid[c1-1][c2])
                        
                    elif (c1%2==0): #If the row number of the current node is even, add the node below the current node to the list of neighbors
                        Neighborlist.append(Grid[c1+1][c2])
                        
                    for node in Neighborlist: #Add all nodes within list of neighbors to the neighbors list of the current node
                    
                        Grid[c1][c2].neighbors.append(node)
                        
                    continue #Skip to the next iteration of the loop
                    
                if ((c2+1)<gridwithinsize): #If the node is within the right edge of the grid, add the node to the right of the current node to the list of neighbors.
                    Neighborlist.append(Grid[c1][c2+1])
                    
                if ((c2-1)>=0): #If the node is within the left edge of the grid, add the node to the left of the current node to the list of neighbors
                    Neighborlist.append(Grid[c1][c2-1])
                    
                if ((c1==0)and(c2==0)): #If the node is at the top left corner of the grid, add all nodes within list of neighbors to neighbors list of current node
                    for node in Neighborlist:
                        
                        Grid[c1][c2].neighbors.append(node)
                        
                    continue
                    
                if ((c1==0)and(c2==(gridwithinsize-1))): #If the node is at the top right corner of the grid...
                    
                    if (c2%2==0): #If the node's column number is even, add all nodes within list of neighbors to neighbors list of current node
                        for node in Neighborlist:
                            Grid[c1][c2].neighbors.append(node)
                        continue
                        
                    else: #If the node's column number is odd, add the node under the current node to the list of neighbors. Then, add all nodes within list of neighbors to neighbors list of current node
                        Neighborlist.append(Grid[c1+1][c2])
                        
                        for node in Neighborlist:
                            
                            Grid[c1][c2].neighbors.append(node)
                            
                        continue
                        
                if ((c2==0)and(c1==(gridsize-1))): #If the node is at the lower left hand corner of the grid...
                    
                    if (c1%2==0): #If the node's row number is even, add the node above it to the list of neighbors
                    
                        Neighborlist.append(Grid[c1-1][c2])
                        
                        for node in Neighborlist: #Add all nodes within list of neighbors to neighbors list of current node
                        
                            Grid[c1][c2].neighbors.append(node)
                            
                        continue
                        
                    else: #If the node's row number is odd, add all nodes within list of neighbors to neighbors list of current node
                    
                        for node in Neighborlist:
                            
                            Grid[c1][c2].neighbors.append(node)
                            
                        continue
                        
                if ((c1==(gridsize-1))and(c2==(gridwithinsize-1))): #If the node is at the lower right corner of the grid...
                
                    Neighborlist.append(Grid[c1-1][c2]) #Add the node above it to the list of neighbors
                    
                    for node in Neighborlist: #Add all nodes within list of neighbors to neighbors list of current node
                    
                        Grid[c1][c2].neighbors.append(node)
                        
                    continue
                    
                if (c1%2==0): #If the row number of the node is even...
                    
                    try: #Catch indexerror exceptions
                    
                        Neighborlist.append(Grid[c1-1][c2]) #Add the node above it to the list of neighbors
                        
                        for node in Neighborlist: #Add all nodes within list of neighbors to neighbors list of current node
                        
                            Grid[c1][c2].neighbors.append(node)
                            
                        continue
                        
                    except:
                        continue
                        
                if (c1%2!=0): #If the row number of the node is odd...
                
                    try: #Catch indexerror exceptions
                    
                        Neighborlist.append(Grid[c1+1][c2]) #Add the node below it to the list of neighbors
                        
                        for node in Neighborlist: #Add all nodes within list of neighbors to neighbors list of current node
                        
                            Grid[c1][c2].neighbors.append(node)
                            
                        continue
                        
                    except:
                        continue


                c2+=1
            c1+=1
            
    def getPotentialDifference(self, node1, node2): #Returns the difference on the voltage between two nodes
    
            return node1.potential - node2.potential;

    def getNodeDistance(self,node1x, node1y,node2x, node2y): #Returns difference between 2 nodes in gridunits
    
            xdist = abs(node1x - node2x);
            ydist = abs(node1y - node2y);
            
            return math.sqrt(math.pow(xdist, 2) + math.pow(ydist, 2));
            
class Node(Simulation): #defines node object properties
    
    neighbors = [];
    external_connections = [];
    
    def __init__(self):
        self.node=node
        
    def __init__(self, atomchargeproportion=None, hybridization=None, potential=None, heat=None):
        self.atomchargeproportion = atomchargeproportion; 
        self.potential = potential;
        self.hybridization = hybridization;
        self.heat = heat;

