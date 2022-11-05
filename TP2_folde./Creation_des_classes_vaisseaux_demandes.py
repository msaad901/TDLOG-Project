from TP1_folder./Creation_des_3_classes_armes import *

class Cruiser(Vessel):
    def __init__(self,coordinates,weapon,max_hits=6):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z>0:
            return "I can't go higher"
        elif z<0:
            return "I can't go lower"
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)

class Submarine(Vessel):
    def __init__(self,coordinates,weapon,max_hits=2):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z!=0 or z!=1:
            return "I can't go there"
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)
        

class Fregate(Vessel):
    def __init__(self,coordinates,weapon,max_hits=5):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z!=0:
            return "I can't go there"
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)


class Destroyer(Vessel):
    def __init__(self,coordinates,weapon,max_hits=4):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z!=0:
            return "I can't go there"
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)


class Aircraft(Vessel):
    def __init__(self,coordinates,weapon,max_hits=1):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z!=1:
            return "I can't go there"
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)
