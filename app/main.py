from perudo import Perudo


# create a new game -> a new instance of the Perudo class
newGame = Perudo()

# run the Perudo game set up class method -> asks the user to input the players
newGame.gameSetUp()

# # rolls the dice for all players and sets activeRound to True
# newGame.roundSetUp()

# newGame.playRound()


newGame.playGame()



# 3 changes to make:
#       - print the current bet before the user has to decide whether to bet or call 
#       - make the outcomes of calling clearer --> which use made the bet,  what was the bet, what will the outcome be 
#       - review all other print statements

# Next fetaures to implement:
#       - removing dice --> new method or add to existing method?
#       - remove players from game --> if noDice == 0 then remove etc 
#       - tie togther rounds by coordinating a game --> will need to add checks on noActivePlayers = 1


# tying together rounds:
#       - create the game   
#       - we need a method of removing players from the game --> when self.noDice = 0 
#       - we need a method of ending the game --> when the total players is 1
