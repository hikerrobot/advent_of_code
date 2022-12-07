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

my_rps = {
    'X':'rock','Y':'paper','Z':'scissors'
}

game_win_rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper' 
}

rps_points = {
    'rock':1,'paper':2,'scissors':3
}

# TODO need to work out the correct piece to match the desired result

# pt1
def round_result_via_compare(score, opponent_choice, my_choice):
    # have we got a draw
    if opponent_choice == my_choice:
        return 3 + score
    # did elf win?
    elif game_win_rules[opponent_choice] == my_choice:
        return 0 + score
    else: # elf lost
        return 6 + score

# pt2
def round_result_via_letter(score, my_choice):
    # have we got a draw
    if "Y" == my_choice:
        return 3 + score
    # did elf win?
    elif "X" ==  my_choice:
        return 0 + score
    else: # Z elf lost
        return 6 + score


def determine_who_won(decoded_round):
    opponent_choice = decoded_round[0]
    my_choice = decoded_round[1]

    # get score for my play piece
    score = rps_points[my_choice]
    print("score type {}, score {} for choice {}".format(type(score), score, my_choice))

    return round_result_via_compare(score, opponent_choice, my_choice)


def decode_round(round):
    if (len(round) != 2):
        sys.exit("invalid round found")

    opponent_choice = elf_opponent_rps[round[0]]
    # print(opponent_choice)
    my_choice = my_rps[round[1]]
    # print(my_choice)
    return [opponent_choice, my_choice]

def process_rounds(game_rounds):

    total_score = 0

    for i in range(len(game_rounds)):
        round = game_rounds[i].split(' ')

        decoded_round = decode_round(round)
        # print("decoded_round {}".format(decoded_round))
        round_result = determine_who_won(decoded_round)
        print("round result {}".format(round_result))
        total_score += round_result
    
    print("total score {}".format(total_score))

process_rounds(file_content)




# def calc_score(round):
