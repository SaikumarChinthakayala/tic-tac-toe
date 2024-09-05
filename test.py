import numpy as np
#fields=np.array([x for x in range(0,3)], [y for y in range(0,3)])
fields=np.array([(x,y) for x in range(0,3) for y in range(0,3)])
print(fields[8])
a=np.empty((3,3))
print(a)
print(a[0,1])

"""
This game will have a board of 3x3 which is called a field and will 9 cells. 
"""
class game():
    def __init__(self):
        self.fields=np.empty([(x,y) for x in range(0,3) for y in range(0,3)])


    def neighbours(self, index):
        picked_cell=self.fields(index)
    

