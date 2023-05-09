from Games.MemoryGame import play as mem_play
from Games.GuessGame import play as guess_play
from Games.CurrencyRouletteGame import play as curr_play
from Utils import Screen_cleaner
from Scores.Score import add_score


def welcome():
    name = input('what is your name: ')
    print('''Hello {} and welcome to the World of Games (WoG)
    Here you can find many cool games to play.\n'''.format(name))
    return name


def load_game():
    while True:
        while True:
            game = input("""Please select a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to
             guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette  - You have to Enter your guess for the value of 1 Dollar in ILS * selected Difficulty
            for the next mathematical calculation:
            (USD in ILS * selected Difficulty  - (5 - Selected Difficulty), USD in ILS * selected Difficulty + (5 - Selected Difficulty)):""")
            while game < '1' or game > '3':
                print('Please select only between 1 - 3')
                game = input()

            if game == '1':
                print(' You select 1. Memory game\n')
                game_name = 'MemoryGame'
                play_func = mem_play
            if game == '2':
                print(' You select 2. Guess game\n')
                game_name = 'GuessGame'
                play_func = guess_play
            if game == '3':
                print(' You select 3. currency roulette\n')
                game_name = 'CurrencyRouletteGame'
                play_func = curr_play
            if game.isdigit():
                break
        game = int(game)

        while True:
            difficulty = input('Please select game difficulty from 1 to 5 where 1 is the lowest and 5 is the highest: ')

            while difficulty < '1' or difficulty > '5':
                print('Please choose only between 1 - 5')
                difficulty = input('Please select game difficulty from 1 to 5 where 1 is the lowest and 5 is the highest: ')

            if difficulty == '1':
                print('Your difficulty is', difficulty)
            elif difficulty == '2':
                print('Your difficulty is', difficulty)
            elif difficulty == '3':
                print('Your difficulty is', difficulty)
            elif difficulty == '4':
                print('Your difficulty is', difficulty)
            elif difficulty == '5':
                print('Your difficulty is', difficulty)
            else:
                print('\n')
            if difficulty.isdigit():
                break
        difficulty = int(difficulty)

        if game == 1:
            game_name = 'MemoryGame'  # replace this with the game name you want to import
            game_module = __import__('Games.' + game_name, fromlist=[''])
            mishak = game_module.play(difficulty)

            if mishak:
                Screen_cleaner()
                add_score(difficulty)

        if game == 2:
            game_name = 'GuessGame'  # replace this with the game name you want to import
            game_module = __import__('Games.' + game_name, fromlist=[''])
            mishak = game_module.play(difficulty)

            if mishak:
                add_score(difficulty)
                Screen_cleaner()
        if game == 3:
            game_name = 'CurrencyRouletteGame'  # replace this with the game name you want to import
            game_module = __import__('Games.' + game_name, fromlist=[''])
            mishak = game_module.play(difficulty)

            if mishak:
                Screen_cleaner()
                add_score(difficulty)



        while True:
            again = input('if you want play again in this game with the same difficulty write Again   //   if you want to choose another game write Game  //  if you want to exit write Exit: ')
            if again == 'again' or again == 'Again':
                mishak = play_func(difficulty)
                if mishak:
                    Screen_cleaner()
                    add_score(difficulty)


            elif again == 'game' or again == 'Game':
                Screen_cleaner()
                load_game()

            elif again == 'exit' or again == 'Exit':
                Screen_cleaner()
                exit()