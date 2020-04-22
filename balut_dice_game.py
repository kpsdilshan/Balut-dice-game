import random

class contestant:  
    def __init__(self, name, rank):  
        self.name = name  
        self.rank = rank

players = []

def display_rules():
    print("\n----WELCOME TO THE BALUT DICE GAME----\n")
    print("\nThe game can be played with 1 ti 4 players")
    print('The Rules are:,','\n'
          'In Balut each player gets 5 dices to roll up.','\n'
          'Making a set of dices or straight will be the goal of the game.','\n'
          'The player one who get the highest score will win the whole game.','\n'
          'The hands of the game ranked as follows: 5 of same number, 4 of same number, 3 of same number, two of same number or the highest number.','\n')
    

def welcome():
    
    
    player_count = input("How may palyers are there: ")
    
    if(int(player_count)<1 or int(player_count)>4):
        welcome()    
        
    for i in range(int(player_count)):
        player_name = input("Enter the player's name: ")
        players.append(contestant(player_name,0))    

    for player in players:
        print(player.name, player.rank, sep=' ')
        
    print("\n")

def game():
    for player in players:
        name=player.name
        rank=player.rank
        dices = []
        number_of_dices = 5
        
        
        #playing the game and get values.
        for i in range(number_of_dices):
            dices.append(random.randint(1,6))

        
        print(dices)
        ranking(player,dices)

def ranking(player,dices):
    #giving the rank to players

    straight_1 = [1,2,3,4,5]
    straight_2 = [2,3,4,5,6]
    
    for i in range(6):
        if(dices.count(i)==5):
            player.rank=1
            print(player.name, " has 5 of same number ")
            return

    if(all(elements in dices for elements in straight_1) or all(elements in dices for elements in straight_2)):
        player.rank=2
        return

    for i in range(6):
        if(dices.count(i)==4):
            player.rank=3
            print(player.name, " has 4 of same number ")
            return
                
    for i in range(6):
        if(dices.count(i)==3):
            player.rank=4
            print(player.name, " has 3 of same number ")
            return
                
    for i in range(6):
        if(dices.count(i)==2):
            player.rank=5
            print(player.name, " has 2 of same number ")
            return
            
    for i in range(6,0,-1):
        count = 1
        if(i in dices):
            player.rank=5+count
            print(player.name, "\'s highest number is ",i)
            return
        count+=1 
    
    
def select_the_winner():
    
    best_rank=11
    for player in players:
        if(player.rank<best_rank):
            best_rank = player.rank

    for player in players:
        if(player.rank==best_rank):
            print("\n",player.name," is the winner\n")

    
response = "y"
while(response=="y"):
   players = []
   display_rules()
   welcome()
   game()
   select_the_winner()

   response =  input("\nAre you want to play again (y/n): ")
