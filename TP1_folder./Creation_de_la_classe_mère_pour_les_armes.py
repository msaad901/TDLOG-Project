class Weapon:
    def __init__(self,ammunitions,range):
        self.amo=ammunitions
        self.range=range

    def fire_at(self,x,y,z):
        return "fire_at("+str(x)+","+str(y)+","+str(z)+")"
