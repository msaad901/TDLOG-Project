from tp1 import *


class Vessel:
    def __init__(self,coordinates,max_hits,weapon):
        self.coord=coordinates
        self.max_hits=max_hits
        self.weapon=weapon

    def go_to(self,x,y,z):
        if self.max_hits==0:
            return('DestroyedError')
        else:
            
            self.coord=(x,y,z)
            return "I go to ("+str(x)+","+str(y)+","+str(z)+")"
    
    def get_coordinates(self):
        print(self.coord)

    def fire_at(self,x,y,z):
        if self.max_hits==0:
            return 'DestroyedError'
        else:
            return self.weapon.fire_at(x,y,z)
