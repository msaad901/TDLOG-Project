class espace:
    vaisseau=[]
    vaisseau_coordinates=[]
    def __init__(self):
        pass
    @classmethod
    def ajouter_vaisseau(cls,new_vaisseau):
        if new_vaisseau.get_coordinates() not in cls.vaisseau_coordinates:
            cls.vaisseau.append(new_vaisseau)
            cls.vaisseau_coordinates.append(new_vaisseau.get_coordinates())
    
    @classmethod
    def recevoir_vaisseau(cls,coordinate):
        if coordinate in cls.vaisseau:
            return True
        else:
            return False
