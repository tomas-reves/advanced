from roulette_model import RouletteGame

number_bet_input = None
place_number_bet_amount = None
color_bet_input = None
place_color_bet_amount = None
odds_evens_bet_input = None
place_odds_evens_bet_amount = None
dozens_bet_input = None
place_dozens_bet_amount = None
low_high_nums_bet_input = None
place_low_high_nums_bet_amount = None
columns_bet_input = None
place_columns_bet_amount = None
dict_of_bets = {}

while True:

    print("==========================================================")
    game_input = int(input(f"ENTER NUMBER TO SELECT GAME\n 1 -- Guess roulette number\n 2 -- Guess color of the number\n "
                           "3 -- Guess odds or evens\n 4 -- Guess dozens\n 5 -- Guess low or high numbers\n 6 -- Guess"
                           "columns\n 7 -- Finish bet and play "))
    print("==========================================================")
    if game_input == 1:
        while True:
            number_of_num_bets = int(input("Enter how many numbers you want to place bet on: "))
            for num in range(number_of_num_bets): # allows to place bets on more than one number
                number_bet_input = int(input("Enter the number from 0 to 36 "))
                place_number_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
                dict_of_bets[number_bet_input] = place_number_bet_amount
            break

    if game_input == 2:
        while True:
            color_bet_input = input("Enter color: red or black ")
            place_color_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
            break
    if game_input == 3:
        while True:
            odds_evens_bet_input = input("Enter odd or even ")
            place_odds_evens_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
            break
    if game_input == 4:
        while True:
            dozens_bet_input = input("Enter dozens: 1st 12, 2nd 12 or 3rd 12 ")
            place_dozens_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
            break
    if game_input == 5:
        while True:
            low_high_nums_bet_input = input("Low numbers (1-18), High numbers (19-36), enter: low or high ")
            place_low_high_nums_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
            break
    if game_input == 6:
        while True:
            columns_bet_input = input("Enter: 1st column, 2nd column or 3rd column")
            place_columns_bet_amount = int(input("Enter your bet for this game, the winning will be 2 to 1: "))
            break
    if game_input == 7:
        roulette_game_obj = RouletteGame()
        if number_bet_input != None:
            for k, v in dict_of_bets.items():
                roulette_game_obj.number_game(k, v)

        if color_bet_input != None:
            roulette_game_obj.color_game(color_bet_input, place_color_bet_amount)

        if odds_evens_bet_input != None:
            roulette_game_obj.even_odd_game(odds_evens_bet_input, place_odds_evens_bet_amount)

        if dozens_bet_input != None:
            roulette_game_obj.dozen_game(dozens_bet_input, place_dozens_bet_amount)

        if low_high_nums_bet_input != None:
            roulette_game_obj.low_high_game(low_high_nums_bet_input, place_low_high_nums_bet_amount)

        if columns_bet_input != None:
            roulette_game_obj.columns_game(columns_bet_input, place_columns_bet_amount)

        print(f"Your winnings: {roulette_game_obj.winnings} EUR")
        break



