width = int(input())
length = int(input())

cake_pieces = width * length
stop_flag = False

while cake_pieces > 0:
    pieces_taken = input()
    if pieces_taken == 'STOP':
        stop_flag = True
        break
    else:
        cake_pieces -= int(pieces_taken)

if stop_flag:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')

