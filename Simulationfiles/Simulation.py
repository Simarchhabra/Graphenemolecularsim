class Simulation:
        
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
        c1=0;
        c2=0;
        
        gridsize=len(Grid)
        gridwithinsize=len(Grid[0])
        
        print gridwithinsize
        print gridsize
        
        for list01 in Grid:
            for Node1 in list01:
                Neighborlist=[] #tells node which nodes surround it
                
                if ((c1>0)and(c1<gridsize)and(c2>0)and(c2<gridwithinsize)):
                    Neighborlist.append(Grid[c1][c2+1])
                    Neighborlist.append(Grid[c1][c2-1])
                    
                    if (c1%2>0):
                        Neighborlist.append(Grid[c1-1][c2])
                        
                    elif (c1%2==0):
                        Neighborlist.append(Grid[c1+1][c2])
                        
                    Grid[c1][c2].neighbors=Neighborlist
                    continue
                    
                if ((c2+1)<gridwithinsize):
                    Neighborlist.append(Grid[c1][c2+1])
                    
                if ((c2-1)>=0):
                    Neighborlist.append(Grid[c1][c2-1])
                    
                if ((c1==0)and(c2==0)):
                    Grid[c1][c2].neighbors=Neighborlist
                    continue
                    
                if ((c1==0)and(c2==(gridwithinsize-1))):
                    
                    if (c2%2==0):
                        Grid[c1][c2].neighbors=Neighborlist
                        continue
                        
                    else:
                        Neighborlist.append(Grid[c1+1][c2])
                        Grid[c1][c2].neighbors=Neighborlist
                        continue
                        
                if ((c2==0)and(c1==(gridsize-1))):
                    
                    if (c1%2==0):
                        Neighborlist.append(Grid[c1-1][c2])
                        Grid[c1][c2].neighbors=Neighborlist
                        continue
                        
                    else:
                        Grid[c1][c2].neighbors=Neighborlist
                        continue
                        
                if ((c1==(gridsize-1))and(c2==(gridwithinsize-1))):
                    Neighborlist.append(Grid[c1-1][c2])
                    Grid[c1][c2].neighbors=Neighborlist
                    continue
                    
                if (c1%2==0):
                    
                    try:
                        Neighborlist.append(Grid[c1-1][c2])
                        Grid[c1][c2].neighbors=Neighborlist
                        continue
                        
                    except:
                        continue
                        
                if (c1%2!=0):
                    try:
                        Neighborlist.append(Grid[c1+1][c2])
                        Grid[c1][c2].neighbors=Neighborlist
                        continue
                        
                    except:
                        continue


                c2+=1
            c1+=1



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
        