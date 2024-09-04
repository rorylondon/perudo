import random 
import perudo as p

class Player():

    def __init__(self, name: str):
        '''
        Inititalises the Player component Class instances for a given player.

        Args:
            - name: str describing the player name inputted by the user.
        '''
        # instance attributes
        self.name = name 
        self.noDice= 1      # each player starts with 5 dice 
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
        # reset the dice cup from previous rounds
        self.cupDice = {i:0 for i in range(1,7)}    

        # for the number of dice remaining, randomly generate a dice value    
        for i in range(self.noDice):
            num = random.randint(1,6)       
            self.cupDice[num] +=1
        print('Player.rollDice METHOD STARTS')
        print(f'{self.name} just rolled the following {self.cupDice}. Nice!')
        print('========================================')

    

    