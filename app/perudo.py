
from player import Player


class Perudo:

    noPlayers=0 
    playerList=[] # populated by gameSetUp class method --> user inputs player names as strings --> then sequentially passed to child class to instantiate child objects --> potential redundancy 
    childInstanceList=[]
    totalDice=0
    currentBet={'quantity':0, 'value':1} # used to track the last bet, instantiated with the last bet 
    currentTurnIndex=0 #used to track the current go 
    activeGame=True
    activeRound=False

    def __init__(self):
        pass


    @classmethod
    def gameSetUp(cls):
        # accept players as user-inputted strings and appends them to class attribute list 'playerList'
        player='_'
        while player!='':
            player=input('Press [ENTER] to start, or enter a player name to add players to the game.')
            if player=='':
                print('========================================')
                print(f'Starting Game with {cls.playerList}')
                print('========================================')
            else:
                cls.playerList.append(player)
                print(f'You just added {player} to the game')
        for playerName in cls.playerList:
            newPlayer = Player(playerName)
            Perudo.childInstanceList.append(newPlayer)

    @classmethod
    def incrementNoDice(cls, amount: int):
        cls.totalDice += amount

    @classmethod
    def incrementNoPlayers(cls, amount: int):
        cls.noPlayers += amount
    




    @classmethod
    def playGame(cls):
        print('========================================')
        print('PLAYGAME METHOD START')
        print('========================================')
        cls.activeGame=True

        while cls.activeGame:
            cls.roundSetUp()
            cls.playRound()

        print('PLAYGAME METHOD END')
        

    @classmethod
    def roundSetUp(cls):
        print('========================================')
        print('ROUND SET UP METHOD STARTS')
        print(f'Total Dice = {cls.totalDice}')
        print('========================================')

        # flags round as begun programatically
        cls.activeRound=True

        # review current players --> remove any players with no dice  
        prevRoundChildInstanceList = cls.childInstanceList

        newList = []
        for i in prevRoundChildInstanceList:
            if i.noDice > 0:
                newList.append(i)
            else:
                pass
        cls.childInstanceList=newList


        # roles the dice for all the players
        for i in cls.childInstanceList:
            i.rollDice()
        # prints to the players the round has begun 
        print(f'The round has begun')
        print('ROUND SET UP METHOD ENDS')

        if len(cls.childInstanceList) == 1:
            cls.activeGame=False

        # TO DO: TRIGGER THE TURN TAKING PROCESS --> should this call nextTurn()? should i

    @classmethod
    def endGame(cls):
        print(f'GAME OVER - {cls.childInstanceList[0]} WINS !!!!!')
        cls.activeGame=False


    @classmethod
    def playRound(cls):
        print('========================================')
        print('PLAYROUND METHOD STARTS')
        print('========================================')
        while cls.activeRound:
            currentTurnString = cls.playerList[cls.currentTurnIndex]
            print('========================================')
            print(f"It is {currentTurnString}'s turn!")
            print('========================================')

            # for the Player instance whos turn it is --> they will take their turns 
            cls.takeTurn()
        print('PLAYROUND METHOD ENDS')
            


    @classmethod
    def takeTurn(cls):
        print('===================================')
        print('TAKE TURN METHOD STARTS')
        print('===================================')
        prevBet=cls.currentBet
        currTurn=cls.currentTurnIndex
        playList=cls.playerList
        print(f'The current bet is {prevBet} made by {playList[currTurn-1]}')
        turnChoice = input('Please select 1 to call the bet, or 2 to raise the bet.')
        if turnChoice=='1':
            print(f'{playList[currTurn]} called the bet of {prevBet} made by {playList[currTurn-1]}')
            cls.callBet()
        elif turnChoice=='2':
            print(f'{playList[currTurn]} chose to raise the current bet of {prevBet} made by {playList[currTurn-1]}')
            cls.makeBet()
        cls.currentTurnIndex = (cls.currentTurnIndex + 1) % len(cls.playerList)
        print('===================================')
        print('TAKETURN METHOD ENDS')
        print('===================================')





    
    @classmethod
    def makeBet(cls) -> str:
        print('MAKEBET METHOD STARTS')
        print(f'The current bet is {cls.currentBet}')
        currentQuantity=cls.currentBet['quantity']
        currentValue=cls.currentBet['value']

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
        print(f"{cls.playerList[cls.currentTurnIndex]} successfully bet {quantityDice} {valueDice}'s")
        print('MAKEBET METHOD ENDS')

    @classmethod
    def callBet(cls)->str:
        print('===================================')
        print('CALLBET METHOD STARTS')
        print('===================================')
        cls.activeRound = False

        # create all dice dict for counting all dice across all players 
        allDiceDict = {i:0 for i in range(1,7)}

        # FUTURE WORK --> Hierarchy as reusable code for reference --> either logic or hard coding 
        # question --> where should the logic to remove dice and or players go? an 'endRound()' function?? is that overly verbose & complicated?
        # values to change: total dice, current bet, playerList, current turn index, active game, active round 
        
        # tally up all the dice for all players
        for i in cls.childInstanceList:
            playerCup = i.cupDice
            for j in playerCup:
                allDiceDict[j] += playerCup[j]
        print(f'ALL DICE DICT{allDiceDict}')

        # compare the last bet to the count of all dice 
        actualQuantity = allDiceDict[cls.currentBet['value']]
        if actualQuantity >= cls.currentBet['quantity']:
            print(f'The last bet was {cls.currentBet}\nThe actual quantity of dice was {actualQuantity}\nThe player who called the bet ({cls.playerList[cls.currentTurnIndex]}) looses')
            cls.childInstanceList[cls.currentTurnIndex-1].noDice -= 1
        elif actualQuantity < cls.currentBet['quantity']:
            # print(f'The last bet was {cls.currentBet}\nThe actual quantity of dice was {actualQuantity}\nThe player who placed the bet ({cls.playerList[cls.currentTurnIndex-1]}) looses')
            # cls.childInstanceList[cls.currentTurnIndex-1].noDice -= 1
            print(cls.childInstanceList, cls.currentTurnIndex)
        # amend class attributes to reflect lost dice and reset starting bet
        cls.totalDice -= 1
        cls.currentBet={'quantity':0, 'value':1}
        print('===================================')
        print('CALLBET METHOD ENDS')
        print('===================================')
        for i in cls.childInstanceList:
            print(i)

        



    
        
