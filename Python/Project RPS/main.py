from random import choice as RandomChoice
from main_utils import  RPS, GAME_VARS as game_vars, GetRPS, GetExtras, YouWin, YouDrew, YouLose
from shop import GetShop
 

def main(game_vars):
    while True:
        user = input('Rock, Paper, Scissors?\n>').casefold().strip()
        user = GetRPS(user)
        if user in RPS:
            ai = RandomChoice(RPS)
            game = {'rock': z, 'paper': YouWin, 'scissors': YouLose} if ai == 'rock' else \
                   {'rock': YouLose, 'paper': YouDrew, 'scissors': YouWin} if ai == 'paper' else \
                   {'rock': YouWin, 'paper': YouLose, 'scissors': YouDrew}
            game_vars = game[user](game_vars)
        
        elif user in ['store', 'shop']:
            game_vars = GetShop(game_vars)
                    
        else:
            game_vars = GetExtras(user, game_vars)


main(game_vars)

            
