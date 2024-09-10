
from player import Player


class Perudo:

    noPlayers=0 
    playerList=[] # populated by gameSetUp class method --> user inputs player names as strings --> then sequentially passed to child class to instantiate child objects --> potential redundancy 
    activePlayerList=[]
    totalDice=0
    currentBet={'quantity':0, 'value':1} # used to track the last bet, instantiated with the last bet 
    currentTurnIndex=0 #used to track the current go 
    activeGame=False
    activeRound=False
    roundTurn=1
    roundNo=1

    def __init__(self):
        pass


    @classmethod
    def gameSetUp(cls):
        ''' 
        Invites the user to input the names of the players, instantiates a Player Class instance for each and appends to a list for reference.

        args:
            - cls.playerList accepted as the empty list defined in the class definition
        out:
            - cls.playerList Player class instances appended upon initialsation triggered by each user input (player name)

        '''
        player='_'
        while player!='':
            player=input('Press [ENTER] to start, or enter a player name to add players to the game.')
            if player=='':
                print('========================================')
                print(f'Starting Game with {[i.name for i in cls.playerList]}')
                print('========================================')
                
            else:
                # instantiate a component Player Class instance using the user supplied name and flags as active player
                cls.playerList.append(Player(player))
                print(f'You just added {player} to the game')
        
        




    @classmethod
    def incrementNoDice(cls, amount: int):
        '''
        Increments the total number of active dice in the game.
        
        args:
            cls: class reference - class attributes being used for state management.
            amount: int denoting how much to increment the total number of active dice by. This will only ever by +5 when a new player is added to the game or -1 at the end of each round.
        '''
        cls.totalDice += amount

    @classmethod
    def incrementNoPlayers(cls, amount: int):
        '''
        Increments the total number of active players in the game.

        args:
            cls: class reference - class attributes being used for state management.
            amount: int denoting how much to increment the total number of active players by.This will only ever by +1 when a new player is added to the game or -1 when a player is eliminated.
        '''        
        cls.noPlayers += amount
    



    @classmethod
    def playGame(cls):
        '''
        Orchestrates the game by flagging the game as being active and recursively setting up and playing rounds by calling the respective class methods, untill the game is no longer active.

        
        args:
            cls: class reference - class attributes being used for state management.
            - cls.activeGame accepted as False - game has not yet begun

        cls attributes:
            - cls.activeGame assigned to True indicating the game has begun

        '''
        print('========================================')
        print('PLAYGAME METHOD START')
        print('========================================')

        # flag game as having begun
        cls.activeGame = True

        while cls.activeGame:
            cls.roundSetUp()
            if not cls.activeGame:
                break
            cls.playRound()
        
        print(f'GAME OVER - {cls.activePlayerList[0]} WINS !!!!!!!!!!!!!!!!!!!!!')
        print('========================================')
        print('PLAYGAME METHOD END')
        print('========================================')

    @classmethod
    def roundSetUp(cls):
        '''
        Sets up the round by removing any players with no dice, rolling dice for all active players and flaggin round to be active after first evaluating if the game is still active (there is more than one active player).
        
        '''
        # if there is only 1 player remaining, they have won and the game should end
        # this logic should be moved --> the roundSetUp should not be called if there is one player remaining. If it needs to be called, it needs to be exited and the rest of the function skipped if condition is true 

        print('========================================')
        print('ROUND SET UP METHOD STARTS')
        print('========================================')



        print(f'Total Dice = {cls.totalDice}')



        # tag any players with no dice as not being active players --> will not be included in the following rounds 
        for i in cls.playerList:
            i.toggleActivePlayer()
        
        cls.activePlayerList = [i for i in cls.playerList if i.activePlayer == True]

        if len(cls.activePlayerList) <= 1:
            cls.activeGame=False
        else:
            # roles the dice for all the players
            for i in cls.activePlayerList:
                i.rollDice()
            # prints to the players the round has begun 
            print(f'The round has begun')

        print('========================================')
        print('ROUND SET UP METHOD ENDS')
        print('========================================')





    @classmethod
    def playRound(cls):
        '''
        Orchestrates the round by conditionally printing current player-turn, and calling the takeTurn method while the round is active. 
        '''
        print('========================================')
        print('PLAYROUND METHOD STARTS')
        print('========================================')


        # flags round as begun programatically
        # should this logic go here?
        # flagging round as active --> this is a condition for the playRound while loop which conditionally calls the takeTurn method 
        # n.b. the takeTurn method seems to be continuously called --> there may be a problem with this implementation currently 
        cls.activeRound=True
        
        
        # if the callBet method has not been called, the round will be active 
        # active round flagged as True in the roundSetUp function, flagged as False in callBet method
        while cls.activeRound:
            # the list this is based on needs to be reviewed --> may need to combine the playerList & child instance list, also need to review turn asignment & management logic --> may need to review takeTurn method
            currentTurnString = cls.playerList[cls.currentTurnIndex].name
            print('========================================')
            print(f"It is {currentTurnString}'s turn!")
            print('========================================')

            # for the Player instance whos turn it is --> they will take their turns 
            cls.takeTurn()
        print('PLAYROUND METHOD ENDS')
            

# may need to review the logic and approach of assigning turns 
# need to add some logic to force the first turn to bet --> should we add a turn counter which defaults to 1 each round and subsequently increments?
    @classmethod
    def takeTurn(cls):
        '''
        Invites players to take their turn, printing the current player-turn and conditionally making or calling a bet based on the user choice.  
        '''
        print('===================================')
        print('TAKE TURN METHOD STARTS')
        print('===================================')

        if cls.roundTurn == 1:
            print(f"It is {cls.playerList[cls.currentTurnIndex].name}'s turn. Please start the betting.")
            cls.makeBet()
        else:
            print(f'The current bet is {cls.currentBet} made by {cls.playerList[cls.currentTurnIndex-1].name}')
            # ADD LOGIC TO EVALUATE TURN --> IF TURN 1, USER CANNOT CALL THE BET 
            turnChoice = input('Please select 1 to call the bet, or 2 to raise the bet.')
            if turnChoice=='1':
                print(f'{cls.playerList[cls.currentTurnIndex].name} called the bet of {cls.currentBet} made by {cls.playerList[cls.currentTurnIndex-1].name}')
                cls.callBet()
            elif turnChoice=='2':
                print(f'{cls.playerList[cls.currentTurnIndex].name} chose to raise the current bet of {cls.currentBet} made by {cls.playerList[cls.currentTurnIndex-1].name}')
                cls.makeBet()
        # increments the turn by continuously lopping through the list
        # EXTRA LOGIC REQUIRED - the player who looses a dice takes the first turn of the next round
        cls.currentTurnIndex = (cls.currentTurnIndex + 1) % len(cls.activePlayerList)

        # increment the round turn counter
        cls.roundTurn += 1
        print('===================================')
        print('TAKETURN METHOD ENDS')
        print('===================================')


    
    @classmethod
    def makeBet(cls) -> str:
        '''
        Orchestrates bets being made by Players after they chose to do so in the takeTurn method. Conditionally updates the current bet if the user-bet is valid.
        '''
        print('MAKEBET METHOD STARTS')
        print(f'The current bet is {cls.currentBet}')

        # assigning dice quantities for greater readability
        currentQuantity=cls.currentBet['quantity']
        currentValue=cls.currentBet['value']


        # should validBet default to True? 
        validBet = False

        while not validBet:
            try:
                quantityDice = int(input("Enter the quantity of dice: "))
                valueDice = int(input("Enter the dice value (1-6): "))

                # Input validation
                if valueDice < 1 or valueDice > 6:
                    print("Invalid dice value. Please enter a number between 1 and 6.")
                    continue 

                # Validate the bet according to the game rules
                if quantityDice > currentQuantity:
                    validBet = True
                elif quantityDice == currentQuantity and quantityDice > currentValue:
                    validBet = True
                else:
                    print("This is not a valid bet, please try again.")

            except ValueError:
                print("Invalid input. Please enter valid integers.")

        # Update the current bet
        cls.currentBet['quantity'] = quantityDice
        cls.currentBet['value'] = valueDice
        print(f"{cls.playerList[cls.currentTurnIndex].name} successfully bet {quantityDice} {valueDice}'s")
        print('MAKEBET METHOD ENDS')

    @classmethod
    def callBet(cls)->str:
        '''
        Ends the round, counts all dice of all players and compares this to the current bet.
        '''
        print('===================================')
        print('CALLBET METHOD STARTS')
        print('===================================')

        # create all dice dict for counting all dice across all players 
        allDiceDict = {i:0 for i in range(1,7)}

        # FUTURE WORK --> Hierarchy as reusable code for reference --> either logic or hard coding 
        # question --> where should the logic to remove dice and or players go? an 'endRound()' function?? is that overly verbose & complicated?
        # values to change: total dice, current bet, playerList, current turn index, active game, active round 
        
        # tally up all the dice for all players
        for i in cls.playerList:
            playerCup = i.cupDice
            for j in playerCup:
                allDiceDict[j] += playerCup[j]
        print(f'ALL DICE DICT{allDiceDict}')


        # assigns the integer count of the value of total dice for the dice value (1-6) of the called bet
        actualQuantity = allDiceDict[cls.currentBet['value']]
        # logic to determine round loser
        if actualQuantity >= cls.currentBet['quantity']:
            # REVIEW PRINT STATEMENTS TO MAKE MORE INTUATIVE
            # TURN MANAGEMENT
            print(f'The last bet was {cls.currentBet}\nThe actual quantity of dice was {actualQuantity}\nThe player who called the bet ({cls.playerList[cls.currentTurnIndex].name}) loses')
            # WHAT IS THE BEST PRACTISE AROUND A COMPOSITE CLASS ALTERING CLASS INSTANCE ATTRIBUTES OF A COMPONENT CLASS?
            cls.playerList[cls.currentTurnIndex].noDice -= 1
        elif actualQuantity < cls.currentBet['quantity']:
            # TURN MANAGEMENT
            print(f'The last bet was {cls.currentBet}\nThe actual quantity of {cls.currentBet} was {actualQuantity}\nThe player who placed the bet ({cls.playerList[cls.currentTurnIndex-1].name}) loses')
            cls.playerList[cls.currentTurnIndex-1].noDice -= 1
 

        # amend class attributes to reflect lost dice and reset starting bet
        # 'round clean up activites' --> WOULD A ROUNDCLEANUP() FUNCTION BE CLEANER?
        cls.totalDice -= 1
        cls.roundTurn = 1
        cls.roundNo += 1
        cls.currentBet = {'quantity':0, 'value':1}
        cls.activeRound = False


        print('===================================')
        print('CALLBET METHOD ENDS')
        print('===================================')



    # # NEED TO REVIEW THIS --> NEVER ACTUALLY BEEN INTEGRATED INTO THE GAME
    # @classmethod
    # def endGame(cls):
    #     print(f'GAME OVER - {cls.playerList[0]} WINS !!!!!')
    #     cls.activeGame=False
    # This could be used to loop the game back round the gameSetUp by asking the user 'Would you like to play again?'

        
