from shop_utils import shop, shopItems, GetItem
 

def GetShop(game_vars):
    message = '\nWelcome to the Booster Store.\n>'
    while True:
        user = input(message).casefold()
        message = 'Anything else?\n>'
        if user.startswith('buy') and user != 'buy':
            game_vars = GetItem(user, game_vars)

        elif user.startswith('item'):    
            [print(f'{item} {"."*(30 - len(f"{item}"))} {item.price}G') for item in shop]
            message = '\nMade yer mind yet?\n>'
        
        elif user in ['exit', 'quit', 'no' if message.startswith('A') else 'leave']:
            return game_vars
        
        else:
            message='Huh?\n>'

        
