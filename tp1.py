
class Weapon:
    def __init__(self,ammunitions,range):
        self.amo=ammunitions
        self.range=range

    def fire_at(self,x,y,z):
        return "fire_at(",x,",",y,",",z,")"


class Lance_missiles_antisurface(Weapon):
    def __init__(self,ammunitions=30,range=40):
        super().__init__(ammunitions,range)

    def fire_at(self,x,y,z):
        if self.amo==0:
            return "NoAmmunitionError"

        elif z!=0:
            return "OutOfRangeError"
            self.amo-=1
        else:
            super().fire_at(x,y,z)

class Lance_missiles_antiair(Weapon):

    def __init__(self,ammunitions=40,range=50):
        super().__init__(ammunitions,range)

    def fire_at(self,x,y,z):
        if self.amo==0:
            return "NoAmmunitionError"

        elif z<=0:
            return "OutOfRangeError"
            self.amo-=1
        else:
            super().fire_at(x,y,z)


class Lance_torpilles(Weapon):

    def __init__(self,ammunitions=20,range=15):
        super().__init__(ammunitions,range)

    def fire_at(self,x,y,z):
        if self.amo==0:
            return "NoAmmunitionError"

        elif z>0:
            self.amo-=1
            return "OutOfRangeError"
            
        else:
            super().fire_at(x,y,z)


    

    




