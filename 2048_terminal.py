# written entirely by Christopher Becher, Oct 2023

from logic import *

def move(inp, gamearr):
    score_add = 0
    moved = 0

    if inp == '0':
        exit()
    elif inp == 'lost':
        gamearr[0] = [2,4,2,4]
        gamearr[1] = [4,2,4,2]
        gamearr[2] = [64,128,2,4]
        gamearr[3] = [0,0,64,2]
    elif inp == 'ahead':
        gamearr[0] = [512,64,128,128]
        gamearr[1] = [64,2,4,64]
        gamearr[2] = [32,128,128,4]
        gamearr[3] = [0,0,64,32]
    elif inp == 'winner':
        gamearr[0][1] = 1024
        gamearr[0][2] = 512
        gamearr[0][3] = 512
    elif inp == '9':
        gamearr[0] = [0,0,0,0]
        gamearr[1] = [0,0,0,0]
        gamearr[2] = [0,0,0,0]
        gamearr[3] = [0,0,0,0]
        add_num(gamearr)
        add_num(gamearr)
        return 0
    elif inp == 'd':
        gamearr, moved, score_add = move_right(gamearr)
    elif inp == 'a':
        gamearr, moved, score_add = move_left(gamearr)
    elif inp == 's':
        gamearr, moved, score_add = move_down(gamearr)
    elif inp == 'w':
        gamearr, moved, score_add = move_up(gamearr)
    else:
        print("Invalid key!")
        return 0
    
    return gamearr, moved, score_add


def main():
    iter = 1
    score = 0
    input_opts = "w = up, a = left, s = down, d = right, 9 = restart, 0 = quit\n"

    print("Let's make 2048!")
    gamearr = start()    
    print_matrix(gamearr)

    while True:
        iter += 1

        gamearr, moved, scoreadd = move(input(input_opts), gamearr)
        score += scoreadd

        if moved == 1:
            add_num(gamearr)
            check_winloss(gamearr)
            print_matrix(gamearr)
            print(f"Turn {iter}, score: {score}\n")

main()
