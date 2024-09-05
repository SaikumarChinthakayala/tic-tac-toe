import numpy as np
"""
This game will have a board of 3x3 which is called a field and will 9 cells. 
"""
class game():
    def __init__(self):
        self.fields=np.empty((3,3))

    @staticmethod
    def NeighbourIndices(index):
        if not isinstance(index, tuple):
            raise Exception("Index needs to be a tuple")
        return [(x,y) for x in range(index[0]-1, index[0]+2) for y in range(index[1]-1, index[1]+2) if (x,y) != index if ({x,y}).issubset({0,1,2})]
        
    

if __name__ == "__main__":
    g=game()
    #print(g.fields)
    print(g.NeighbourIndices((2,2)))
