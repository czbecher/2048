import random
import copy

def print_matrix(gamearr):
    displaytable = {
        0: "  0   ",
        2: "  2   ",
        4: "  4   ",
        8: "  8   ",
        16: " 16   ",
        32: " 32   ",
        64: " 64   ",
        128: " 128  ",
        256: " 256  ",
        512: " 512  ",
        1024: "1024  ",
        2048: "2048  ",
    }

    gamearr_str = " - - - - -  - - - - - \n"
    for row in gamearr:
        for col in row:
            gamearr_str += displaytable[col]
        gamearr_str += "\n\n"
    gamearr_str = gamearr_str[:-1] + " - - - - -  - - - - - "
    print(gamearr_str)

def add_num(gamearr):
    # 1. make a list of all available coordinates
    # 2. choose a random value in the list
    # 3. add a 2 or a 3 there
    valid_cells = []
    for row_index in range(4):
        for col_index in range(4):
            if gamearr[row_index][col_index] == 0:
                valid_cells.append([row_index,col_index])

    random_valid_cell = random.sample(valid_cells, 1)[0]            # choose cell from list
    newtile = random.choices([2,4], [0.9,0.1], k=1)[0]              # 90% chance of 2, else 4
    gamearr[random_valid_cell[0]][random_valid_cell[1]] = newtile   # add val

    return gamearr

def start():
    gamearr = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    add_num(gamearr)
    add_num(gamearr)

    return gamearr

def check_winloss(gamearr):
    # returns 2 if there's a win (if 2048 is in gamearr)
    # returns 1 if there's a loss (if 0 is not in gamearr)
    # returns 0 if the game should continue

    if any(2048 in row for row in gamearr):
        return 2
    elif all(0 not in row for row in gamearr):
        game_copy = copy.deepcopy(gamearr)
        move_right(game_copy)
        move_left(game_copy)
        move_up(game_copy)
        move_down(game_copy)
        if gamearr == game_copy:
            return 1
        else:
            return 0

    else:
        return 0

def move_right(gamearr):
    game_copy = copy.deepcopy(gamearr)
    score_increase = 0

    for row_index in [0,1,2,3]:
        invalid_col_index = []
        for col_index_from in [2,1,0]:      # work backward from the rightmost-1 column to the leftmost
            cell_val = gamearr[row_index][col_index_from]
            if cell_val != 0:
                col_index_dest = col_index_from+1

                # search the cells to the right, stop when there's something other than 0 or its the last col
                for i in range(col_index_dest,4,1):   
                    if i in invalid_col_index:
                        break
                    elif gamearr[row_index][i] == cell_val:   # if cell to the right has the same val, it's a good dest cell
                        col_index_dest = i
                        break
                    elif gamearr[row_index][i] != 0:    # if cell to the right has a non-zero val, it's a bad dest cell, choose the previous
                        break
                    col_index_dest = i  # if cell to right has a 0 val, it's a good dest cell, but check the next one
            
                end_val = gamearr[row_index][col_index_dest]

                if end_val == 0:
                    gamearr[row_index][col_index_dest] = end_val + cell_val
                    gamearr[row_index][col_index_from] = 0

                elif end_val == cell_val:
                    score_increase = end_val + cell_val
                    gamearr[row_index][col_index_dest] = score_increase
                    gamearr[row_index][col_index_from] = 0
                    invalid_col_index.append(col_index_dest)

    is_valid = gamearr != game_copy
    return gamearr, is_valid, score_increase

def move_left(gamearr):
    game_copy = copy.deepcopy(gamearr)
    score_increase = 0

    for row_index in [0,1,2,3]:
        invalid_col_index = []
        for col_index_from in [1,2,3]:      # work backward from the leftmost-1 column to the rightmost
            cell_val = gamearr[row_index][col_index_from]
            if cell_val != 0:
                col_index_dest = col_index_from-1

                # search the cells to the right, stop when there's something other than 0 or its the last col
                for i in range(col_index_dest,-1,-1):   
                    if i in invalid_col_index:
                        break
                    elif gamearr[row_index][i] == cell_val:   # if cell to the left has the same val, it's a good dest cell
                        col_index_dest = i
                        break
                    elif gamearr[row_index][i] != 0:    # if cell to the left has a non-zero val, it's a bad dest cell, choose the previous
                        break
                    col_index_dest = i  # if cell to left has a 0 val, it's a good dest cell, but check the next one
            
                end_val = gamearr[row_index][col_index_dest]

                if end_val == 0:
                    gamearr[row_index][col_index_dest] = end_val + cell_val
                    gamearr[row_index][col_index_from] = 0

                elif end_val == cell_val:
                    score_increase = end_val + cell_val
                    gamearr[row_index][col_index_dest] = score_increase
                    gamearr[row_index][col_index_from] = 0
                    invalid_col_index.append(col_index_dest)

    is_valid = gamearr != game_copy
    return gamearr, is_valid, score_increase

def move_down(gamearr):
    game_copy = copy.deepcopy(gamearr)
    score_increase = 0

    for col_index in [0,1,2,3]:
        invalid_row_index = []
        for row_index_from in [2,1,0]:      # work backward from the bottom-1 row to the top
            cell_val = gamearr[row_index_from][col_index]
            if cell_val != 0:
                row_index_dest = row_index_from+1

                # search the cells below, stop when there's something other than 0 or its the last row
                for i in range(row_index_dest,4,1):   
                    if i in invalid_row_index:
                        break
                    elif gamearr[i][col_index] == cell_val:   # if cell below has the same val, it's a good dest cell
                        row_index_dest = i
                        break
                    elif gamearr[i][col_index] != 0:    # if cell below has a non-zero val, it's a bad dest cell, choose the previous
                        break
                    row_index_dest = i  # if cell below has a 0 val, it's a good dest cell, but check the next one
            
                end_val = gamearr[row_index_dest][col_index]

                if end_val == 0:
                    gamearr[row_index_dest][col_index] = end_val + cell_val
                    gamearr[row_index_from][col_index] = 0

                elif end_val == cell_val:
                    score_increase = end_val + cell_val
                    gamearr[row_index_dest][col_index] = score_increase
                    gamearr[row_index_from][col_index] = 0
                    invalid_row_index.append(row_index_dest)

    is_valid = gamearr != game_copy
    return gamearr, is_valid, score_increase

def move_up(gamearr):
    game_copy = copy.deepcopy(gamearr)
    score_increase = 0

    for col_index in [0,1,2,3]:
        invalid_row_index = []
        for row_index_from in [1,2,3]:      # work backward from the top-1 row to the bottom
            cell_val = gamearr[row_index_from][col_index]
            if cell_val != 0:
                row_index_dest = row_index_from-1

                # search the cells above, stop when there's something other than 0 or its the last row
                for i in range(row_index_dest,-1,-1):
                    if i in invalid_row_index:
                        break
                    elif gamearr[i][col_index] == cell_val:   # if cell above has the same val, it's a good dest cell
                        row_index_dest = i
                        break
                    elif gamearr[i][col_index] != 0:    # if cell above has a non-zero val, it's a bad dest cell, choose the previous
                        break
                    row_index_dest = i  # if cell above has a 0 val, it's a good dest cell, but check the next one
            
                end_val = gamearr[row_index_dest][col_index]

                if end_val == 0:
                    gamearr[row_index_dest][col_index] = end_val + cell_val
                    gamearr[row_index_from][col_index] = 0

                elif end_val == cell_val:
                    score_increase = end_val + cell_val
                    gamearr[row_index_dest][col_index] = score_increase
                    gamearr[row_index_from][col_index] = 0
                    invalid_row_index.append(row_index_dest)

    is_valid = gamearr != game_copy
    return gamearr, is_valid, score_increase

def random_move(gamearr):  #returns the function itself
    return random.sample([move_up, move_down, move_left, move_right], 1)[0](gamearr)

def get_score(gamearr):
    total_sum = sum(value for row in gamearr for value in row)

    sum = 0
    for row in gamearr:
        for val in row:
            sum += val
    return sum

def move(inp, gamearr):
    game_copy = copy.deepcopy(gamearr)
    score_add = 0
    valid_move = 0

    if inp == '0' or inp == '/opt/homebrew/bin/python3 /Users/riipen/Desktop/Python/2048/2048.py':
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
        gamearr, valid_move, score_add = move_right(gamearr)
    elif inp == 'a':
        gamearr, valid_move, score_add = move_left(gamearr)
    elif inp == 's':
        gamearr, valid_move, score_add = move_down(gamearr)
    elif inp == 'w':
        gamearr, valid_move, score_add = move_up(gamearr)
    else:
        # print("Invalid key!")
        return 0
    
    return valid_move
    # if gamearr != game_copy:
    #     return 1
    # else:
    #     # print("that did nothing")
    #     return 0


# is_valid = 0
# score = 32
# gamearr = [
#         [2,0,2,0],
#         [0,8,4,0],
#         [0,0,2,0],
#         [0,0,0,0]
#     ]

# print_matrix(gamearr)
# move('a', gamearr)
# # score += scoreadd
# print_matrix(gamearr)
# print(is_valid, score)

