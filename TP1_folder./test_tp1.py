
from Creation_des_3_classes_armes import Lance_missiles_antisurface
from Creation_des_3_classes_armes import Lance_torpilles
from Creation_des_3_classes_armes import Lance_missiles_antiair

from unittest import TestCase


class TestclassTP1(TestCase):

  def testLance_missiles_antisurface(self):
  
    w1=Lance_missiles_antisurface().fire_at(5,7,0)
    self.assertNotEqual("NoAmmunitionError", w1)
    self.assertNotEqual("OutOfRangeError", w1)
    
  def testLance_torpilles(self):
  
    w2=Lance_torpilles().fire_at(10,-4,5)
    self.assertNotEqual("NoAmmunitionError", w2)
    self.assertNotEqual("OutOfRangeError", w2)
    
  def testLance_missiles_antiair(self):
  
    w3=Lance_missiles_antiair.fire_at(100,45,0)
    self.assertNoteEqual("NoAmmunitionError", w3)
    self.assertNotEqual("OutOfRangeError", w3)
