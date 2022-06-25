import random
import time

red_color_roulette_list = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_color_roulette_list = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green_color_roulette_list = [0]



def check_number_color():
    if a in red_color_roulette_list:
        return 1
    elif a in black_color_roulette_list:
        return 2
    else:
        return 3

initial_color = 1
initial_bet = 1
winnings = 1000
game = 0

while True:
    game += 1
    print(f"{winnings}")
    a = random.randint(0, 36)
    if check_number_color() == initial_color:
        if initial_color == 1:
            initial_color = 2
        elif initial_color == 2:
            initial_color = 1
        initial_bet *= 2
        winnings += initial_bet
        initial_bet = 1
    else:
        winnings -= initial_bet
        if initial_color == 1:
            initial_color = 1
            if winnings == 0:
                print(f'{game}')
                break
        elif initial_color == 2:
            initial_color = 2
            if winnings == 0:
                print(f'{game}')
                break

        initial_bet *= 2



# while True:
#
#     print("==========================================================")
#     game_input = int(input(f"ENTER NUMBER TO SELECT GAME\n 1 -- Guess roulette number\n 2 -- Guess color of the number\n "
#                            "3 -- Guess odds or evens\n 4 -- Guess dozens\n 5 -- Guess low or high numbers\n 6 -- Guess "
#                            "columns\n 7 -- Finish bet and play "))
#     print("==========================================================")
#     if game_input == 1:
#         while True:
#             number_of_num_bets = int(input("Enter how many numbers you want to place bet on: "))
#             for num in range(number_of_num_bets): # allows to place bets on more than one number
#                 number_bet_input = int(input("Enter the number from 0 to 36 "))
#                 place_number_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
#                 dict_of_bets[number_bet_input] = place_number_bet_amount
#             break
#
#     if game_input == 2:
#         while True:
#             color_bet_input = input("Enter color: red or black ")
#             place_color_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
#             break
#     if game_input == 3:
#         while True:
#             odds_evens_bet_input = input("Enter odd or even ")
#             place_odds_evens_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
#             break
#     if game_input == 4:
#         while True:
#             dozens_bet_input = input("Enter dozens: 1st 12, 2nd 12 or 3rd 12 ")
#             place_dozens_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
#             break
#     if game_input == 5:
#         while True:
#             low_high_nums_bet_input = input("Low numbers (1-18), High numbers (19-36), enter: low or high ")
#             place_low_high_nums_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
#             break
#     if game_input == 6:
#         while True:
#             columns_bet_input = input("Enter: 1st column, 2nd column or 3rd column")
#             place_columns_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
#             break
#     if game_input == 7:
#         roulette_game_obj = RouletteGame()
#         if number_bet_input != None:
#             for k, v in dict_of_bets.items():
#                 roulette_game_obj.number_game(k, v)
#
#         if color_bet_input != None:
#             roulette_game_obj.color_game(color_bet_input, place_color_bet_amount)
#
#         if odds_evens_bet_input != None:
#             roulette_game_obj.even_odd_game(odds_evens_bet_input, place_odds_evens_bet_amount)
#
#         if dozens_bet_input != None:
#             roulette_game_obj.dozen_game(dozens_bet_input, place_dozens_bet_amount)
#
#         if low_high_nums_bet_input != None:
#             roulette_game_obj.low_high_game(low_high_nums_bet_input, place_low_high_nums_bet_amount)
#
#         if columns_bet_input != None:
#             roulette_game_obj.columns_game(columns_bet_input, place_columns_bet_amount)
#
#         print(f"Your winnings: {roulette_game_obj.winnings} EUR")
#         break



