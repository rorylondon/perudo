import random 
import src.app.perudo as p

class Player():

    def __init__(self, name: str):
        '''
        Inititalises the Player component Class instances for a given player.

        Args:
            - name: str describing the player name inputted by the user.
        '''
        # instance attributes
        self.name = name 
        self.noDice= 5      # each player starts with 5 dice 
        self.cupDice = {i:0 for i in range(1,7)}        # before dice have been rolled --> they have no dice 
        self.activePlayer = True


        # call classmethods in composite class
        # each player starts the game with 5 dice
        p.Perudo.incrementNoDice(5)
        p.Perudo.incrementNoPlayers(1)


    def __str__(self) -> str:
        return f'{self.name} has {self.noDice} dice remaining'

    
    def rollDice(self):
        '''
        Randomly generates the dice values for each player.

        '''
        print('========================================')
        print('ROLL DICE METHOD STARTS')
        print('========================================')
        # reset the dice cup from previous rounds
        self.cupDice = {i:0 for i in range(1,7)}    

        # for the number of dice remaining, randomly generate a dice value    
        for i in range(self.noDice):
            num = random.randint(1,6)       
            self.cupDice[num] +=1
        print('Player.rollDice METHOD STARTS')
        print(f'{self.name} just rolled the following {self.cupDice}. Nice!')
        print('========================================')
        print('ROLL DICE METHOD ENDS')
        print('========================================')


    def toggleActivePlayer(self):
        '''
        Flags players as inactive if they have no dice. They will be filtered out in the Perudo.activePlayerList when generated each round.

        '''
        print('========================================')
        print('TOGGLE ACITVE PLAYER METHOD STARTS')
        print('========================================')
        if self.noDice < 1:
            self.activePlayer = False
            print(self.name, 'Lost their lost dice, and with that they are eliminated from the game.')
        else:
            pass

        print('========================================')
        print('TOGGLE ACTIVE PLAYER METHOD ENDS ')
        print('========================================')

    

    