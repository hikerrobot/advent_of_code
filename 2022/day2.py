import sys
# each line in the file is a round

# 2 dicts, one for each player.
# score dict, to provide points

# score is only reqd for your result, i.e. from the second column

# round is scored as follows:
# shape + result
# shape values, rock 1 paper 2 scissors 3
# result: lose 0 draw 3 win 6

# only need to track your score.
# answer: calculate your total score

foo_input = ['C X', 'A Y', 'A Z', 'B Y', 'C Y']

elf_opponent_rps = {
    'A':'rock','B':'paper','C':'scissors'
}

my_rps = {
    'X':'rock','Y':'paper','Z':'scissors'
}

# rock beats scissors

game_win_rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper' 
}

rps_points = {
    'rock':1,'paper':2,'scissors':3
}

def determine_who_won(decoded_round):
    opponent_choice = decoded_round[0]
    my_choice = decoded_round[1]

    # have we got a draw
    if opponent_choice == my_choice:
        return 3
    # did elf win?
    elif game_win_rules[opponent_choice] == my_choice:
        return 0
    else: # elf lost
        return 6

def decode_round(round):
    if (len(round) != 2):
        sys.exit("invalid round found")

    opponent_choice = elf_opponent_rps[round[0]]
    print(opponent_choice)
    my_choice = my_rps[round[1]]
    print(my_choice)
    return [opponent_choice, my_choice]

def process_rounds(game_rounds):
    for i in range(len(game_rounds)):
        round = game_rounds[i].split(' ')

        decoded_round = decode_round(round)
        print("decoded_round {}".format(decoded_round))
        round_result = determine_who_won(decoded_round)
        print("round result {}".format(round_result))

process_rounds(foo_input)




# def calc_score(round):
