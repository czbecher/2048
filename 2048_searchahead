# The code for the function ai_move specifically is taken directly from this Kite video: https://www.youtube.com/watch?v=FE_oAQ5FzMk, Oct 2023
# I personally wrote the code in this file and logic.py
# In the video, he sets searches_per_move to 20 and search_length to 10,
#   and gets 2048 on the first try.  For me, it can't get past 1024.

from logic import *
import copy

def ai_move(board, searches_per_move, search_length):
    first_moves = [move_right, move_left, move_up, move_down]
    scores = [0,0,0,0]

    for first_index in range(4):                                    # try all four possible first moves
        first_board = copy.deepcopy(board)
        first_move = first_moves[first_index]
        first_board, first_valid, first_score = first_move(first_board)

        if first_valid:
            add_num(first_board)
            scores[first_index] += first_score
        else:
            continue

        for later_moves in range(searches_per_move):                # try x sets of random moves after the first move
            move_number = 1
            search_board = copy.deepcopy(first_board)
            is_valid = True

            while is_valid and move_number < search_length:         # try x random moves for this set and return the new score
                search_board, is_valid, score = random_move(search_board)
                if is_valid:
                    add_num(search_board)
                    scores[first_index] += score
                    move_number += 1

        # print(f"\nOption {first_index} could lead to:")
        # print_matrix(search_board)

    best_move_index = scores.index(max(scores))
    # print(f"\nChoosing option {best_move_index}: of {scores}")
    best_move = first_moves[best_move_index]
    return best_move(board)


def main():
    print("New 2048 Game:")
    max = 0
    iter = 0
    score = 0
    gamearr = start()
    print_matrix(gamearr)

    while True:                         # checks if you want to continue every max moves
        max += 1000
        while iter < max:
            gamearr, _ , scoreadd = ai_move(gamearr, 20, 10)    # this is the recommended settings, but it's never gotten past 1024 with this
            if scoreadd == 0:
                if check_winloss(gamearr) == 1:
                    print_matrix(gamearr)
                    print("AI Lost ☹")
                    return iter, score
            
            add_num(gamearr)
            score += scoreadd
            iter += 1
            # print_matrix(gamearr)
            # print(f"Turn {iter}, score: {score}")
            if iter % 100 == 0:         # prints the matrix and score every 100 moves
                print_matrix(gamearr)
                print(f"Turn {iter}, score: {score}")


        if check_winloss(gamearr) == 2:
            print("AI Won !")

        print_matrix(gamearr)
        print(f"Turn {iter}, score: {score}")
        if input("Continue? N to stop ").lower() == "n":
            break


# scores = []
# for _ in range(20):
turns, score = main()
print(f"Turn {turns}, score: {score}\n")
#     scores.append(score)

# print(scores)
