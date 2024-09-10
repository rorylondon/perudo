# import unittest
# from scripts.utils import Perudo

import os 
import sys

print(sys.path)


# class TestStringMethods(unittest.TestCase):

#     def setUp(self):
#         self.game = Perudo()

#     # def tearDown(self):
#     #     self.game.dispose()

#     def test_no_players(self):
#         self.assertEqual(self.game.noPlayers, 0) 
    



# # Why is this logic required --> why not just call the unittest.main() method to execute all the tests?
# if __name__ =='__main__':
#     # executing the built in .main() method calls all tests 
#     unittest.main()


# # setUp() method --> can be used to avoid reduncant test cases, by providing set up steps which apply to many tests - e.g. instantiating objects (Perudo/Player)


# # things we want to test
# # - players are added to the game 
# # - bets work 
# # - a dice is lost each round 
# # - taking turns --> call or bet triggers each method respectively 
# # - players are eliminated when they get 0 dice 
# # - a player wins when they are the last player 
# # - class attributes are tracked and change correctkly
# # -
