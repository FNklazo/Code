game_vars = {'gold': 10, 'inv': []}
shop = {'apple': 5, 'banana': 10}

def trans_check(purchase):
    def wrapper(pocket, store, amount, bill=0):
        while (bill:=store['apple'] * amount) > pocket['gold']:
            amount -= 1
            if amount < 1:
                print('Your pockets are shallow. Too shallow.\n')
                return pocket
        return purchase(pocket, store, amount, bill)
    return wrapper

@trans_check
def purchase(pocket, store, amount, bill=0):
    user = input(f'Buy apple? ').casefold()
    if user.startswith('y'):
        pocket['inv'] += ['Apple']
        pocket['gold'] -= store['apple']
    else:
        print('Ok, thx for window shopping.')
    return game_vars

print(8%3)

