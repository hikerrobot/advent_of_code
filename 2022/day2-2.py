import sys, logging

sys.path.append('../')

import read_file as rf

# logger = logging.getLogger('aoclogger')
logging.basicConfig(level=logging.INFO)
# logger.setLevel(logging.INFO)
file_content = rf.get_file_contents('input-d2')



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
    'rock':'scissors',
    'paper':'rock',
    'scissors':'paper'
}

rps_points = {
    'rock':1,'paper':2,'scissors':3
}

outcome = {
    'X':'lose','Y':'draw','Z':'win'
}

def round_result_via_known_outcome(opponent_choice, round_outcome):
    logging.debug("opponent choice: {}, round outcome: {}".format(opponent_choice, outcome[round_outcome]))
    if round_outcome == 'X': #lose
        my_choice = game_lose_rules[opponent_choice]
        logging.debug("lose, my choice {}".format(my_choice))
        return rps_points[my_choice]
    elif round_outcome == 'Y': #draw
        my_choice = opponent_choice
        logging.debug("draw, my choice {}".format(my_choice))
        return 3 + rps_points[my_choice]
    else: # win 'Z'. could add check here to error if not known.
        my_choice = game_win_rules[opponent_choice]
        logging.debug("win, my choice {}".format(my_choice))
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
    logging.info("game rounds = {}".format(len(game_rounds)))

    for i in range(len(game_rounds)):
        round = game_rounds[i].split(' ')

        decoded_round = decode_round(round)
        logging.debug("decoded_round {}".format(decoded_round))
        round_result = determine_who_won(decoded_round)
        logging.debug("round result {}".format(round_result))
        total_score += round_result
        logging.debug("=======================================")
    
    logging.info("total score {}".format(total_score))

process_rounds(file_content)


