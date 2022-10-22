from shop_utils import GetItem


RPS = 'rock', 'paper', 'scissors'
GAME_VARS = {'inv':[], 'gold':0, 'streak':0, 'prev_streak':0, 'chances':3, 'multiplier':1}


def YouWin(game_vars):
    print('You Win!\n')
    game_vars['streak'] += 1
    if not game_vars['streak'] % 3:
        print('+1 Gold!\nStreak Saved!\n')
        game_vars['gold'] += 1
        game_vars['prev_streak'] = game_vars['streak']
    return game_vars

def YouDrew(game_vars):
    print('Draw!\n')
    return game_vars

def YouLose(game_vars):
    print('You Lose!\n')
    game_vars['chances'] -= 1
    if game_vars['chances'] <= 0:
        print('Streak Lost!\n')
        game_vars['streak'], game_vars['multiplier'], game_vars['chances'] = 0, 1, 3
    return game_vars

def GetRPS(user, RPS=RPS):
    if user:
        u_buffer = [choice for choice in RPS if choice.startswith(user)]
        user = u_buffer[0] if u_buffer else user
    return user

def GetExtras(user, game_vars):
    if user in ['e', 'inv', 'inventory']:
        print(game_vars['inv']) if game_vars['inv'] else print('Your inventory is empty.\n')
    
    elif user.startswith('use'):
        item = GetItem(user, game_vars, game_vars['inv'])
        if item:
            game_vars = item[0].Use(game_vars)
        else:
            print('\nYou do not own this item.\n')
    
    elif user in ['stats', 'gold', 'streak']:
        print(f"\nStreak: {game_vars['streak']}\n"
              f"Gold: {game_vars['gold']}\n")
    else:
        print('...')
    return game_vars
