
class Weapon:
    def __init__(self,ammunitions,range):
        self.amo=ammunitions
        self.range=range

    def fire_at(self,x,y,z):
        print("fire_at(",x,",",y,",",z,")")


class Lance_missiles_antisurface(Weapon):
    def __init__(self,ammunitions=30,range=40):
        super().__init__(ammunitions,range)

    def fire_at(self,x,y,z):
        if self.amo==0:
            print("NoAmmunitionError")

        elif z!=0:
            print("OutOfRangeError")
            self.amo-=1
        else:
            super().fire_at(x,y,z)

class Lance_missiles_antiair(Weapon):

    def __init__(self,ammunitions=40,range=50):
        super().__init__(ammunitions,range)

    def fire_at(self,x,y,z):
        if self.amo==0:
            print("NoAmmunitionError")

        elif z<=0:
            print("OutOfRangeError")
            self.amo-=1
        else:
            super().fire_at(x,y,z)


class Lance_torpilles(Weapon):

    def __init__(self,ammunitions=20,range=15):
        super().__init__(ammunitions,range)

    def fire_at(self,x,y,z):
        if self.amo==0:
            print("NoAmmunitionError")

        elif z>0:
            print("OutOfRangeError")
            self.amo-=1
        else:
            super().fire_at(x,y,z)


"""
lance_mi_anti_sur=Lance_missiles_antisurface()
lance_torp=Lance_torpilles()
lance_mi_anti_air=Lance_missiles_antiair()

lance_mi_anti_air.fire_at(5,7,5)
lance_torp.fire_at(10,-4,5)
lance_mi_anti_sur.fire_at(100,45,0)
"""

