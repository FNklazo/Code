class shopItems():
    def __init__(self, name, price, stack=0):
        self.name, self.price, self.stack = name, price, stack

    def __repr__(self):
        return self.name

    def __eq__(self, o):
        return str(self).casefold().startswith(o)

    def TranscationCheck(self, game_vars, amount):
        while (cost:=self.price * amount) > game_vars['gold']:
            amount -= 1  
            if amount < 1:
                print('Your pockets are shallow. Too shallow.\n')
                return game_vars
        return self.purchase(game_vars, amount, cost)          

    def Purchase(self, game_vars, amount, cost):
        user = input(f'Purchase [x{amount} {self}]? (y/N)\n>').casefold()
        if user.startswith('y'):
            game_vars['inv'] += [self]
            game_vars['gold'] -= cost
            print('Your patronage is appreciated.\n')
        else:
            print('Transaction cancelled.\n')
        return game_var

    def Use(self, game_vars):
        if self == res_str.name:
            game_vars = UseRestoreStreak(game_vars)
        elif self == jeop.name:
            game_vars = UseJeopardy(game_vars)
        else:
            game_vars = UseFreedom(game_vars)

        self.stack -= 1
        game_vars['inv'] -= [self] if self.stack < 1 else 'DO_NOTHING'

        return game_vars


shop = res_str, jeop, fd = shopItems('Restore Streak', 3), shopItems('Jeopardy', 5), shopItems('Freedom', 75)


def GetItem(user, game_vars, array=shop):
    user = user.split(' ')
    item = [s_item for s_item in array if s_item == user[1]]
    if array != game_vars['inv']:
        amount = int(user[-1]) if user[-1].isnumeric() else 1
        if item and amount > 0:
            game_vars = item[0].TranscationCheck(game_vars, amount)
        else:
            print("I don't have what you're looking for.\n")
        return game_vars
    return item

def UseRestoreStreak(game_vars):
    if game_vars['prev_streak'] > game_vars['streak'] > 0:
        game_vars['streak'] = game_vars['prev_streak']
        game_vars['prev_streak'] = 0
        print('Streak Restored!\n')
    else:
        print('Conditions not met.\n')
    return game_vars

def UseJeopardy(game_vars):
    game_vars['multiplier'] *= 3
    game_vars['chances'] = 1
    print('Multiplier Increased!\n')
    return game_vars

def UseFreedom(game_vars):
    print('run away...\nthe summer time dont await for me.\n')
    

    