import random
import time
import Live
import os
from Utils import Screen_cleaner
def generate_sequence(difficulty):
    secret_sequence = [random.randint(1, 101) for i in range(int(difficulty))]
    return secret_sequence

def get_list_from_user():
    user_input = input("Please enter your numbers: ")
    user_list = [int(no) for no in user_input.split()]
    return user_list

def is_list_equal(secret_sequence, user_list):
    if secret_sequence == user_list:
        return True
    else:
        return False



def play(difficulty):


    secret_sequence = generate_sequence(difficulty)
    print(secret_sequence)
    Screen_cleaner()
    result = is_list_equal(secret_sequence, get_list_from_user())


    if result:
        print("Congratulations! You've won.")
        return True
    else:
        print("Sorry, better luck next time.")
        return False
