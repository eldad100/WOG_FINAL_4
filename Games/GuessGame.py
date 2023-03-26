import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number




def get_guess_from_user(difficulty):

    number = input(f' guess a number between 1 to {difficulty}: ')
    if number.isdigit() and int(number) >= 1 and int(number) <= difficulty:
        return int(number)
    else:
        print("Invalid input, please enter a number between 1 to", difficulty)



def compare_results(number, secret_number):
    if number == secret_number:
        return True
    else:
        return False









def play(difficulty):
    secret_number = generate_number(difficulty)
    number = get_guess_from_user(difficulty)
    result = compare_results(number, secret_number)
    if result:
        print("YOU WON!")
        return True
    else:
        print(f'The number was {secret_number}')
        return False





