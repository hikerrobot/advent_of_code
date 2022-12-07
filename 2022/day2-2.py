import sys

sys.path.append('../')

import read_file as rf

file_content = rf.get_file_contents('input-d2')
# print("file lines = {}".format(len(fileContents)))


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

#foo_input = ['C X', 'A Y', 'A Z', 'B Y', 'C Y']

elf_opponent_rps = {
    'A':'rock','B':'paper','C':'scissors'
}

# pt1
my_rps = {
    'X':'rock','Y':'paper','Z':'scissors'
}

game_win_rules = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock' 
}


game_lose_rules = {
    'rock':'paper',
    'paper':'rock',
    'scissors':'rock'
}

rps_points = {
    'rock':1,'paper':2,'scissors':3
}

# TODO need to work out the correct piece to match the desired result
# X means lose
# Y means draw
# Z means win

def round_result_via_known_outcome(opponent_choice, known_outcome):
    print("oc {} outcome {}".format(opponent_choice, known_outcome))
    if known_outcome == 'X': #lose
        my_choice = game_lose_rules[opponent_choice]
        print("lose, my choice {}".format(my_choice))
        return rps_points[my_choice]
    elif known_outcome == 'Y': #draw
        my_choice = opponent_choice
        print("draw, my choice {}".format(my_choice))
        return 3 + rps_points[my_choice]
    else: # win 'Z'. could add check here to error if not known.
        my_choice = game_win_rules[opponent_choice]
        print("win, my choice {}".format(my_choice))
        return 6 + rps_points[my_choice]

def determine_who_won(decoded_round):
    opponent_choice = decoded_round[0]
    known_outcome = decoded_round[1]

    return round_result_via_known_outcome(opponent_choice, known_outcome)


def decode_round(round):
    if (len(round) != 2):
        sys.exit("invalid round found")

    opponent_choice = elf_opponent_rps[round[0]]
    my_choice = round[1]
    return [opponent_choice, my_choice]

def process_rounds(game_rounds):

    total_score = 0
    print("game rounds = {}".format(len(game_rounds)))

    for i in range(len(game_rounds)):
        round = game_rounds[i].split(' ')

        decoded_round = decode_round(round)
        print("decoded_round {}".format(decoded_round))
        round_result = determine_who_won(decoded_round)
        print("round result {}".format(round_result))
        total_score += round_result
        print("=======================================")
    
    print("total score {}".format(total_score))

process_rounds(file_content)




# def calc_score(round):
