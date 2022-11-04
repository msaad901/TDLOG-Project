import Weapon from tp1

from unittest import TestCase


class TestclassTP1(TestCase):

  def testCruiser(self):

    Anti_air=Lance_missiles_antiair()
    Cruiser=Cruiser((1,1,0),Anti_air,6)
    Cruisergo=Cruiser.go_to(1,2,10)
    Cruiserfi=Cruiser.fire_at(10,10,10)

    self.assertNotEqual("I can't go higher", Cruisergo)
    self.assertNotEqual("I can't go lower", Cruisergo)
    self.assertNotEqual('DestroyedError', Cruiserfi)

  def testSubmarine(self):

    lance_torpilles_1=Lance_torpilles()
    Submarine=Submarine((1,1,-1),lance_torpilles_1,2)
    Submarinego=Submarine.go_to(1,2,10)
    Submarinefi=Submarine.fire_at(10,10,10)

    self.assertNotEqual("I can't go there", Submarinego)
    self.assertNotEqual('DestroyedError', Submarinefi)

  def testFregate(self):

    lance_missiles_anti_surface_1=Lance_missiles_antisurface()
    Fregate=Fregate((2,2,0),lance_missiles_anti_surface_1,5)
    Fregatego=Fregate.go_to(1,2,10)
    Fregatefi=Fregate.fire_at(10,10,10)

    self.assertNotEqual("I can't go there", Fregatego)
    self.assertNotEqual('DestroyedError', Fregatefi)

  def testDestroyer(self):

    lance_torpilles_2=Lance_torpilles()
    Destroyer=Destroyer((3,3,0),lance_torpilles_2,4)
    Destroyergo=Destroyer.go_to(1,2,10)
    Destroyerfi=Destroyer.fire_at(10,10,10)

    self.assertNotEqual("I can't go there", Destroyergo)
    self.assertNotEqual('DestroyedError', Destroyerfi)

  def testAircraft(self):

    lance_missiles_anti_surface_2=Lance_missiles_antisurface()
    Aircraft=Aircraft((1,1,1),lance_missiles_anti_surface_2,1)
    Aircraftgo=Aircraft.go_to(1,2,10)
    Aircraftfi=Aircraft.fire_at(10,10,10)
    
    self.assertNotEqual("I can't go there", Aircraftgo)
    self.assertNotEqual('DestroyedError', Aircraftfi)
