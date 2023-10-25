from logic import *

print(start_str)
gamearr = start()    
iter = 1

while True:
    print("\n", iter)
    iter += 1

    print_matrix(gamearr)
    
    moved = move(input(input_opts), gamearr)
    if moved == 1:
        add_num(gamearr)
        check_winloss(gamearr)