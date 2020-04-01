from white import WhitePieces
from black import BlackPieces

count = 0
machine_turn = False
game_alive = True
white_pieces = WhitePieces()
black_pieces = BlackPieces()

#alphabetical values
alpha_values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
}

#chess board
chess_row_one = ['1','♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
chess_row_two = ['2','♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
chess_row_three = ['3','_', '_', '_', '_', '_', '_', '_', '_']
chess_row_four = ['4','_', '_', '_', '_', '_', '_', '_', '_']
chess_row_five = ['5','_', '_', '_', '_', '_', '_', '_', '_']
chess_row_six = ['6','_', '_', '_', '_', '_', '_', '_', '_']
chess_row_seven = ['7','♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']
chess_row_eight = ['8','♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
chess_row_letters = ['', ' A','B', 'C', 'D', 'E', 'F', 'G', 'H']

#row values
row_values = {
    '1': chess_row_one,
    '2': chess_row_two,
    '3': chess_row_three,
    '4': chess_row_four,
    '5': chess_row_five,
    '6': chess_row_six,
    '7': chess_row_seven,
    '8': chess_row_eight,
}

def printer():
    #prints chess board
    print(' '.join(x for x in chess_row_eight))
    print(' '.join(x for x in chess_row_seven))
    print(' '.join(x for x in chess_row_six))
    print(' '.join(x for x in chess_row_five))
    print(' '.join(x for x in chess_row_four))
    print(' '.join(x for x in chess_row_three))
    print(' '.join(x for x in chess_row_two))
    print(' '.join(x for x in chess_row_one))
    print(' '.join(x for x in chess_row_letters))

printer()
#check feature
def check(piece, colour, origin_x, origin_y):
    pass

def kill(dead_piece, colour):
    if colour == 'white':
        del white_pieces.white_pieces[dead_piece]
        del white_pieces.symbols[dead_piece]
    else:
        del black_pieces.black_pieces[dead_piece]
        del black_pieces.black_symbols[dead_piece]


#moving rules for knights
def knight(destination_x, destination_y, origin_x, origin_y):
    adjacent = (abs(int(destination_x) - int(origin_x))) ** 2
    opposite = (abs(int(destination_y) - int(origin_y))) ** 2
    if adjacent + opposite == 5:
        return True
    else:
        return False

#moving rules for pawns
def pawn(destination_x, destination_y, origin_x, origin_y, colour, piece, destination):
    if colour == 'black':
        going_forward = (int(destination_y) - int(origin_y)) * (-1)
    else:
        going_forward = int(destination_y) - int(origin_y)
    adjacent = (abs(int(destination_x) - int(origin_x))) ** 2
    opposite = (abs(int(destination_y) - int(origin_y))) ** 2
    if going_forward > 0:
        chess_row = row_values[destination_y]
        try:
            chess_row_below = row_values[str(int(destination_y) - 1)]
        except KeyError:
            chess_row_below = chess_row
        try:
            chess_row_above = row_values[str(int(destination_y) + 1)]
        except KeyError:
            chess_row_above = chess_row
        #if reaches last row then turns into queen
        if colour == 'white' and destination_y == '8' and (chess_row[destination_x] == '_' or (chess_row[destination_x] in [black_pieces.black_symbols[x] for x in black_pieces.black_symbols])):
            #turn into queen
            white_pieces.white_pieces[str(count)] = destination
            white_pieces.symbols[str(count)] = '♛'
            row_values['8'][destination_x] = '♛'
            del white_pieces.white_pieces[piece]
            del white_pieces.symbols[piece]
            row_values['7'][origin_x] = '_'
            return True
        elif colour == 'black' and destination_y == '1' and (chess_row[destination_x] == '_' or (chess_row[destination_x] in [white_pieces.symbols[x] for x in white_pieces.symbols])):
            black_pieces.black_pieces[str(count)] = destination
            black_pieces.black_symbols[str(count)] = '♕'
            row_values['1'][destination_x] = '♕'
            del black_pieces.black_pieces[piece]
            del black_pieces.black_symbols[piece]
            row_values['2'][origin_x] = '_'
            return True
        if colour == 'white':
            if piece in [x for x in white_pieces.two_step if white_pieces.two_step[x] == True]:
                if (chess_row[destination_x] == '_' and adjacent + opposite == 4) and (chess_row_above[destination_x] == '_'):
                    white_pieces.two_step[piece] = False
                    return True
        elif colour == 'black':
            if piece in [x for x in black_pieces.black_two_step if black_pieces.black_two_step[x] == True]:
                if (chess_row[destination_x] == '_' and adjacent + opposite == 4) and (chess_row_above[destination_x] == '_'):
                    black_pieces.black_two_step[piece] = False
                    return True
        if True:
            if chess_row[destination_x] == '_' and adjacent + opposite == 1:
                if piece in [x for x in white_pieces.two_step if white_pieces.two_step[x] == True]:
                    white_pieces.two_step[piece] = False
                if piece in [x for x in black_pieces.black_two_step if black_pieces.black_two_step[x] == True]:
                    black_pieces.black_two_step[piece] = False
                #only move forward if no pieces are there
                return True
            else:
                #can move diagonal if an opposite piece is there
                if adjacent + opposite == 2 :
                    if colour == 'white' and chess_row[destination_x] in [black_pieces.black_symbols[x] for x in black_pieces.black_symbols]:
                        if piece in [x for x in white_pieces.two_step if white_pieces.two_step[x] == True]:
                            white_pieces.two_step[piece] = False
                    #checks to see if it is following pawn rules
                        return True
                    elif colour == 'black' and chess_row[destination_x] in [white_pieces.symbols[x] for x in white_pieces.symbols]:
                        if piece in [x for x in black_pieces.black_two_step if black_pieces.black_two_step[x] == True]:
                            black_pieces.black_two_step[piece] = False
                        return True
    return False

#moving rules for bishop
def bishop(destination_x, destination_y, origin_x, origin_y, colour):
    count = 0
    width = int(destination_x) - int(origin_x)
    height = int(destination_y) - int(origin_y)
    if (abs(width) == abs(height)) and (height != 0 or width != 0):
        if height > 0:
            try:
                chess_row_above = row_values[str(int(origin_y) + 1)]
            except KeyError:
                return False
            if width < 0:
                for x in range(int(origin_y) + 1, int(destination_y)):
                    count -= 1
                    chess_row_above_check = row_values[str(x)]
                    if colour == 'white':
                        if chess_row_above_check[int(destination_x) - count] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False
                        elif chess_row_above_check[int(destination_x) - count] in [white_pieces.symbols[x] for x in white_pieces.white_pieces]:
                            return False
                    elif colour == 'black':
                        if chess_row_above_check[int(destination_x) - count] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False
                        elif chess_row_above_check[int(destination_x) - count] in [white_pieces.symbols[x] for x in white_pieces.white_pieces]:
                            return False
            elif width > 0:
                for x in range(int(origin_y) + 1, int(destination_y)):
                    count += 1
                    chess_row_above_check = row_values[str(x)]
                    if colour == 'white':
                        if chess_row_above_check[int(origin_x) + count] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False                        
                        elif chess_row_above_check[int(origin_x) + count] in [white_pieces.symbols[x] for x in white_pieces.white_pieces]:
                            return False
                    elif colour == 'black':
                        if chess_row_above_check[int(origin_x) + count] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False
                        if chess_row_above_check[int(origin_x) + count] in [white_pieces.symbols[x] for x in white_pieces.white_pieces]:
                            return False
        elif height < 0:
            try:
                chess_row_below = row_values[str(int(origin_y) - 1)]
            except KeyError:
                return False
            if width > 0:
                for x in range(int(destination_y), int(origin_y)):
                    count -= 1
                    chess_row_below = row_values[str(x)]
                    if colour == 'white':
                        if chess_row_below[int(destination_x) + count] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False
                        elif chess_row_below[int(destination_x) + count] in [white_pieces.symbols[x] for x in white_pieces.white_pieces]:
                            return False
                    elif colour == 'black':
                        if chess_row_below[int(destination_x) + count] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False
                        elif chess_row_below[int(destination_x) + count] in [white_pieces.symbols[x] for x in white_pieces.white_pieces]:
                            return False
            elif width < 0:
                for x in range(int(destination_y), int(origin_y)):
                    count += 1
                    chess_row_below = row_values[str(x)]
                    if colour == 'white':
                        if chess_row_below[count] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False
                        elif chess_row_below[count] in [white_pieces.symbols[x] for x in white_pieces.white_pieces]:
                            return False
                    elif colour == 'black':
                        if chess_row_below[count] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False
                        elif chess_row_below[count] in [white_pieces.symbols[x] for x in white_pieces.white_pieces]:
                            return False
        return True
    return False

#moving rules for king
def king(destination_x, destination_y, origin_x, origin_y):
    width = (abs(int(destination_x) - int(origin_x))) ** 2
    height = (abs(int(destination_y) - int(origin_y))) ** 2
    #1 step diagonal
    if width == 1 and height == 1:
        return True
    elif (width == 0 and height == 1) or (height == 0 and width == 1):
        return True
    return False

#moving rules for queen
def queen(destination_x, destination_y, origin_x, origin_y, colour):
    width = int(destination_x) - int(origin_x)
    height = int(destination_y) - int(origin_y)

    #if it is moving vertically or horizontally
    if height == 0 or width == 0:
        if rook(destination_x, destination_y, origin_x, origin_y, colour):
            print('yes')
            return True
        else:
            return False
    else:
        if (bishop(destination_x, destination_y, origin_x, origin_y, colour)):
            print('yes 2')
            return True
        else:
            return False
    return False

#moving rules for rook
def rook(destination_x, destination_y, origin_x, origin_y, colour):
    width = int(destination_x) - int(origin_x)
    height = int(destination_y) - int(origin_y)
    chess_row = row_values[destination_y]

    if width == 0 or height == 0:
        if width == 0:
            #going vertically
            if height > 0:
                try:
                    chess_row_above = row_values[str(int(origin_y) + 1)]
                except KeyError:
                    return False
                if colour == 'white':
                    for x in range(int(origin_y), int(destination_y)):
                        chess_row_above_check = row_values[str(x)]
                        if chess_row_above_check[int(destination_x)] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces] :
                            return False
                    for x in white_pieces.symbols:
                        if white_pieces.symbols[x] in chess_row_above[int(destination_x)]:
                            return False
                elif colour == 'black':
                    for x in range(int(origin_y), int(destination_y)):
                        chess_row_above_check = row_values[str(x)]
                        if chess_row_above_check[int(destination_y)] in [white_pieces.symbols[x] for x in white_pieces.white_pieces] :
                            return False
                    for x in black_pieces.black_symbols:
                        if black_pieces.black_symbols[x] in chess_row_above[int(destination_x)]:
                            return False
            elif height < 0:
                try:
                    chess_row_below = row_values[str(int(origin_y) - 1)]
                except KeyError:
                    return False
                if colour == 'white':
                    for x in range(int(destination_y), int(origin_y)):
                        chess_row_above_check = row_values[str(x)]
                        if chess_row_above_check[int(destination_y)] in [black_pieces.black_symbols[x] for x in black_pieces.black_pieces]:
                            return False
                    for x in white_pieces.symbols:
                        if white_pieces.symbols[x] in chess_row_below[int(destination_x)]:
                            return False
                elif colour == 'black':
                    for x in range(int(destination_y), int(origin_y)):
                        chess_row_above_check = row_values[str(x)]
                        if chess_row_above_check[int(destination_y)] in [white_pieces.symbols[x] for x in white_pieces.symbols]:
                            return False
                    for x in black_pieces.black_symbols:
                        if black_pieces.black_symbols[x] in chess_row_below[int(destination_x)]:
                            return False
        elif height == 0:
            if width > 0:
                if colour == 'white':
                    for x in range(int(origin_x), int(destination_x)):
                        if chess_row[int(x)] in [black_pieces.black_symbols[x] for x in black_pieces.black_symbols]:
                            return False
                    for x in white_pieces.symbols:
                        if white_pieces.symbols[x] in chess_row[int(destination_x)]:
                            return False
                if colour == 'black':
                    for x in range(int(origin_x), int(destination_x) ):
                        if chess_row[int(x)] in [white_pieces.symbols[x] for x in white_pieces.symbols]:
                            return False
                    for x in black_pieces.black_symbols:
                        if black_pieces.black_symbols[x] in chess_row[int(destination_x)]:
                            return False
            elif width < 0:
                if colour == 'white':
                    for x in range(int(destination_x), int(origin_x)):
                        if chess_row[int(x)] in [black_pieces.black_symbols[x] for x in black_pieces.black_symbols]:
                            return False
                    for x in white_pieces.symbols:
                        if white_pieces.symbols[x] in chess_row[int(destination_x)]:
                            return False
                if colour == 'black':
                    for x in range(int(destination_x), int(origin_x)):
                        if chess_row[int(x)] in [white_pieces.symbols[x] for x in white_pieces.symbols]:
                            return False
                    for x in black_pieces.black_symbols:
                        if black_pieces.black_symbols[x] in chess_row[int(destination_x)]:
                            return False
        return True
    return False    

def mover(current_position, piece, destination, colour):
    #whether to move or not
    answer = False
    #current row and column
    row = row_values[current_position[-1:]]
    column = alpha_values[current_position[:-1]]

    #destination row and column
    square_position_numb = destination[-1:]
    try:
        row_to_move = row_values[square_position_numb]
        square_position_letter = destination[:-1]
        column_to_move = alpha_values[square_position_letter]
    except KeyError:
        printer()
        return False
    #checks if the square is free
    #and if the square doesn't have 
    #a piece of the same colour
    if colour == 'white':
        #piece type of destination square
        if destination not in white_pieces.white_pieces.values():
            #moves for knight
            if piece == 'white_knight_one' or piece == 'white_knight_two':
                if knight(column_to_move, square_position_numb, column, current_position[-1:]):
                    answer = True
            #moves for pawn
            if '♟' == white_pieces.symbols[piece]:
                if pawn(column_to_move, square_position_numb, column, current_position[-1:], 'white', piece, destination):
                    answer = True
            elif '♜' == white_pieces.symbols[piece]:
                if rook(column_to_move, square_position_numb, column, current_position[-1:], 'white'):
                    answer = True
            elif '♝' == white_pieces.symbols[piece]:
                if bishop(column_to_move, square_position_numb, column, current_position[-1:], 'white'):
                    answer = True
            elif '♚' == white_pieces.symbols[piece]:
                if king(column_to_move, square_position_numb, column, current_position[-1:], 'white'):
                    answer = True
            elif '♛' == white_pieces.symbols[piece]:
                if queen(column_to_move, square_position_numb, column, current_position[-1:], 'white'):
                    answer = True

        if answer:
            #gets the piece that was killed (if there was any)
            dead_piece = [x for x in black_pieces.black_symbols if black_pieces.black_pieces[x] == destination]

            #replaces the position with the new piece
            try:
                row_to_move[column_to_move] = white_pieces.symbols[piece]
                white_pieces.white_pieces[piece] = destination
                row[column] = '_'

                #if the piece has killed
                if len(dead_piece) == 1:
                    kill(dead_piece[0], 'black')
            except KeyError:
                printer()
                return True
        else:
            print('Can\'t move there')
    elif colour == 'black':
        answer = False
        if destination not in black_pieces.black_pieces.values():
            #moves for knight
            if piece == 'black_knight_one' or piece == 'black_knight_two':
                if knight(column_to_move, square_position_numb, column, current_position[-1:]):
                    answer = True
            #moves for pawn
            if '♙' == black_pieces.black_symbols[piece]:
                if pawn(column_to_move, square_position_numb, column, current_position[-1:], 'black', piece, destination):
                    answer = True
            if '♖' == black_pieces.black_symbols[piece]:
                if rook(column_to_move, square_position_numb, column, current_position[-1:], 'black'):
                    answer = True
            if '♗' == black_pieces.black_symbols[piece]:
                if bishop(column_to_move, square_position_numb, column, current_position[-1:], 'black'):
                    answer = True
            if '♔' == black_pieces.black_symbols[piece]:
                if king(column_to_move, square_position_numb, column, current_position[-1:], 'black'):
                    answer = True
            if '♕' == black_pieces.black_symbols[piece]:
                if king(column_to_move, square_position_numb, column, current_position[-1:], 'black'):
                    answer = True
                    
        if answer:
            #gets the piece that was killed (if there was any)
            dead_piece = [x for x in white_pieces.white_pieces if white_pieces.white_pieces[x] == destination]

            #replaces the position with the new piece
            row_to_move[column_to_move] = black_pieces.black_symbols[piece]
            black_pieces.black_pieces[piece] = destination
            row[column] = '_'

            #if the piece has killed
            if len(dead_piece) == 1:
                kill(dead_piece[0], 'white')
        else:
            print('Can\'t move there')
    
    printer()
    return answer

while game_alive:
    #user is always white
    #user goes first
    if machine_turn == False:
        current_position = str(input('Piece position to move: '))
        piece = [x for x in white_pieces.white_pieces if white_pieces.white_pieces[x] == current_position]
        destination_position = str(input('Position to move to : '))
        try:
            machine_turn = mover(current_position, piece[0], destination_position, 'white')
            print(machine_turn)
        except IndexError:
            print('Wrong colour piece!')
            machine_turn = False

    else:
        #machine turn
        current_position = str(input('Piece position to move: '))
        piece = [x for x in black_pieces.black_pieces if black_pieces.black_pieces[x] == current_position]
        destination_position = str(input('Position to move to : '))
        try:
            answer = mover(current_position, piece[0], destination_position, 'black')
            if answer == False:
                machine_turn = True
            else:
                machine_turn = False
        except IndexError:
            print('Wrong colour piece!')
            machine_turn = True