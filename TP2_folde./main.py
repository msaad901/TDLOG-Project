



Anti_air=Lance_missiles_antiair()
lance_torpilles_1=Lance_torpilles()
lance_missiles_anti_surface_1=Lance_missiles_antisurface()
lance_torpilles_2=Lance_torpilles()
lance_missiles_anti_surface_2=Lance_missiles_antisurface()

Cruiser=Cruiser((1,1,0),Anti_air,6)
Submarine=Submarine((1,1,-1),lance_torpilles_1,2)
Fregate=Fregate((2,2,0),lance_missiles_anti_surface_1,5)
Destroyer=Destroyer((3,3,0),lance_torpilles_2,4)
Aircraft=Aircraft((1,1,1),lance_missiles_anti_surface_2,1)

Cruiser.go_to(1,2,10)
Cruiser.go_to(1,2,-10)
Cruiser.get_coordinates()
Cruiser.go_to(5,7,0)
Cruiser.get_coordinates()
print(Cruiser.weapon.amo)# affiche le nombre d'amo de l'arme
Cruiser.fire_at(10,10,10)# car c anti_air donc ca marche normal car z>0
Cruiser.fire_at(10,10,-10) #ici ca affiche OutOfRangeError
print(Cruiser.weapon.amo)#le nombre d'amo a diminue de 1 apres OutOfRangeError
