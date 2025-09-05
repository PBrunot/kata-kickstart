from unittest import TestCase
from python3_kickstart import greetings_package

class Test_Greetings_Package(TestCase):
    def test_zero(self):
        self.assertEqual(greetings_package.calcola_punteggio([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), 0)
    
    def test_all_ones(self):
        self.assertEqual(greetings_package.calcola_punteggio([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), 20)
    
    def test_spare(self):
        self.assertEqual(greetings_package.calcola_punteggio([5,5,3]), 13)
    
    def test_strike(self):
        self.assertEqual(greetings_package.calcola_punteggio([10,3,4]), 24)
    
    def test_strike_spare(self):
        self.assertEqual(greetings_package.calcola_punteggio([10,5,5,0,0,0,0]), 30)

    def test_perfect_game(self):
        self.assertEqual(greetings_package.calcola_punteggio([10,10,10,10,10,10,10,10,10,10,10,10]), 300)
    
    