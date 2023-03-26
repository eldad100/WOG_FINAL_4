from currency_converter import CurrencyConverter
import random


def get_money_interval(difficulty):
    madad = CurrencyConverter()
    randoms = random.randint(1, 101)
    print(f'The random number is: {randoms}')

    usd_v = madad.convert(1, "USD", "ILS")
    print('The current value of dolar is: ', usd_v)

    ereh_madad = madad.convert(int(randoms), 'USD', 'ILS')
    hesbon = (ereh_madad -(5-difficulty), ereh_madad+(5-difficulty))
    return hesbon

def get_guess_from_user():
        while True:
            user_input = input("""Enter a decimal number, for example 50.4, between the next interval:
             (random number * USD in ILS  - (5 - Selected Difficulty),random number * USD in ILS + (5 - Selected Difficulty)): """)
            if user_input.count(".") == 1 and user_input.replace(".", "").isdigit():
                return float(user_input)
            print("Invalid input. Please enter a valid decimal number.")




def play(difficulty):
    hasbon_mahsev = get_money_interval(difficulty)
    money_from_user = float(get_guess_from_user())

    if hasbon_mahsev[0] <= money_from_user <= hasbon_mahsev[1]:
        print("You won!")
        return True
    else:
        print(f'The value was between {hasbon_mahsev[0]} and {hasbon_mahsev[1]}')
        print("You lost.")
        return False
