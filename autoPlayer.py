"""
This is version of Assignment 5 Part 2 in which a "computer" plays a full game of Taffy Tangle using the same graphics
module. After selecting the difficulty for the computer, you can watch it execute its desired moves until the
game ends. The AI, named Tandy, is not very smart. Tandy will always do the first valid move it finds. This strategy
allowed me to balance my games difficulty; in the form of the amount of turns, target score ad multipliers, by
running Tandy on each difficulty and calculating its average ending score and using this benchmark as an average
for a typical game. Tandy utilizes the same function in my user oriented script that checks for remaining moves,
(the same one that finds the hint) but instead of doing nothing when finding a move, Tandy will swap the pieces.

"""


import taffyTangleGraphics as tTG
import random
import time


def make_board(max_piece):
    """
    Make a 7x9 2D array that will represent the game board as the game is played out.
    :return: Board the 7x9 array filled with random integers that represent the individual game pieces (6)
    that does not contain any matches of 3.
    """
    board = []
    for r in range(7):
        board.append([])
        for c in range(9):
            random_piece = random.randint(1, max_piece)
            board[r].append(random_piece)
    # Clear any matches that may occur on the starting board and continue to do so until there are no matches.
    clear_matches(board)
    while drop_swap(board, max_piece):
        clear_matches(board)
    return board


def swap(board, r1, c1, r2, c2):
    """
    Swap two different positions on a 2d array given by their index as parameters.
    """
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]


def are_adjacent(r1, c1, r2, c2):
    """
    Test the coordinates of the selected game pieces to see if they are adjacent horizontally or vertically only.
    :param r1: The row of the first selected piece.
    :param c1: The column of the first selected piece.
    :param r2:  The row of the second selected piece.
    :param c2: The column of the second selected piece.
    :return: True if the two pieces are directly adjacent. False, if they are not.
    """
    tests = [(r1 == r2) and (c1+1 == c2),
             (c1 == c2) and (r1+1 == r2),
             (r1 == r2) and (c1-1 == c2),
             (c1 == c2) and (r1-1 == r2)]
    # Try all circumstances where the selected pieces are adjacent pieces (only vertically or horizontally).
    for i in range(len(tests)):
        try:
            if tests[i]:
                return True
        except IndexError:
            continue
    return False


def same_pieces(a, b, c, d=None, e=None):
    """
    This function checks a given amount of game pieces (min. 3, up to 5) if they are numerically the same and not
    empty spaces (0) in the array that represents the game board.
    :param a: The first piece in question.
    :param b: The second piece in question.
    :param c: The third piece in question
    :param d: The fourth piece in question, None if no 4th parameter is passed.
    :param e: The fifth piece in question, None if no 5th parameter is passed.
    :return: True, if the given pieces are the same. False otherwise.
    """
    if d is None and e is None:
        if (a % 10) == (b % 10) == (c % 10) and (a and b and c) != 0:
            return True
        return False
    if e is None:
        if (a % 10) == (b % 10) == (c % 10) == (d % 10) and (a and b and c and d) != 0:
            return True
        return False
    if (a % 10) == (b % 10) == (c % 10) == (d % 10) == (e % 10) and (a and b and c and d and e) != 0:
        return True
    return False


def clear_matches(board, multiplier=None):
    """
    This function checks each location on the board for a potential match of every possible shape in my game.
    Minimum 3 in a row ranging up to 5 pieces in L or T shapes.
    :param board: The 2D array representing the current game board to be analyzed.
    :param multiplier: The multiplier applied to the turn score based on the selected difficulty.
    :return: turn_score * 100, will represent the attained score for the user that turn or subsequent matches from
    falling pieces.
    """
    time.sleep(0.2)
    turn_score = 0
    # + Plus sign. Can only occur from a falling formation...
    for r in range(1, len(board)-1):
        for c in range(1, len(board[r])-1):
            if same_pieces(board[r][c], board[r+1][c], board[r-1][c], board[r][c+1], board[r][c-1]):
                board[r][c] = 0
                board[r+1][c] = 0
                board[r-1][c] = 0
                board[r][c+1] = 0
                board[r][c-1] = 0
                turn_score += 7
    # 5 Horizontal in a row (visually 5 vertically).
    for r in range(len(board)):
        for c in range(len(board[r])-4):
            if same_pieces(board[r][c], board[r][c+1], board[r][c+2], board[r][c+3], board[r][c+4]):
                board[r][c] = 0
                board[r][c+1] = 0
                board[r][c+2] = 0
                board[r][c+3] = 0
                board[r][c+4] = 0
                turn_score += 6
    # 5 Vertically in a row (visually 5 horizontally).
    for r in range(len(board)-4):
        for c in range(len(board[r])):
            if same_pieces(board[r][c], board[r+1][c], board[r+2][c], board[r+3][c], board[r+4][c]):
                board[r][c] = 0
                board[r+1][c] = 0
                board[r+2][c] = 0
                board[r+3][c] = 0
                board[r+4][c] = 0
                turn_score += 6
    # Matches of 5 (T and L Shapes).
    for r in range(len(board)):
        for c in range(len(board[r])):
            # L shape
            if r in range(len(board) - 2) and c in range(len(board[0]) - 2) and \
                    same_pieces(board[r][c], board[r+1][c], board[r+2][c], board[r][c+1], board[r][c+2]):
                board[r][c] = 0
                board[r+1][c] = 0
                board[r+2][c] = 0
                board[r][c+1] = 0
                board[r][c+2] = 0
                turn_score += 5
            if r in range(2, len(board)) and c in range(len(board[0]) - 2) and \
                    same_pieces(board[r][c], board[r-1][c], board[r-2][c], board[r][c+1], board[r][c+2]):
                board[r][c] = 0
                board[r-1][c] = 0
                board[r-2][c] = 0
                board[r][c+1] = 0
                board[r][c+2] = 0
                turn_score += 5
            if r in range(len(board) - 2) and c in range(2, len(board[0])) and \
                    same_pieces(board[r][c], board[r+1][c], board[r+2][c], board[r][c-1], board[r][c-2]):
                board[r][c] = 0
                board[r+1][c] = 0
                board[r+2][c] = 0
                board[r][c-1] = 0
                board[r][c-2] = 0
                turn_score += 5
            if r in range(2, len(board)) and c in range(2, len(board[0])) and \
                    same_pieces(board[r][c], board[r-1][c], board[r-2][c], board[r][c-1], board[r][c-2]):
                board[r][c] = 0
                board[r-1][c] = 0
                board[r-2][c] = 0
                board[r][c-1] = 0
                board[r][c-2] = 0
                turn_score += 5
            # T shape (visually upside down)
            if r in range(len(board)-2) and c in range(1, len(board[0])-1) and \
                    same_pieces(board[r][c], board[r+1][c], board[r+2][c], board[r][c+1], board[r][c-1]):
                board[r][c] = 0
                board[r+1][c] = 0
                board[r+2][c] = 0
                board[r][c+1] = 0
                board[r][c-1] = 0
                turn_score += 5
            # T shape (visually sideways -|)
            if r in range(2, len(board)) and c in range(1, len(board[0])-1) and \
                    same_pieces(board[r][c], board[r-1][c], board[r-2][c], board[r][c+1], board[r][c-1]):
                board[r][c] = 0
                board[r-1][c] = 0
                board[r-2][c] = 0
                board[r][c+1] = 0
                board[r][c-1] = 0
                turn_score += 5
            # T shape (visually T)
            if r in range(1, len(board)-1) and c in range(2, len(board[0])) and \
                    same_pieces(board[r][c], board[r][c-1], board[r][c-2], board[r+1][c], board[r-1][c]):
                board[r][c] = 0
                board[r][c-1] = 0
                board[r][c-2] = 0
                board[r+1][c] = 0
                board[r-1][c] = 0
                turn_score += 5
            if r in range(1, len(board)-1) and c in range(len(board[0])-2) and \
                    same_pieces(board[r][c], board[r+1][c], board[r-1][c], board[r][c+1], board[r][c+2]):
                board[r][c] = 0
                board[r+1][c] = 0
                board[r-1][c] = 0
                board[r][c+1] = 0
                board[r][c+2] = 0
                turn_score += 5
    # 4 Horizontal in a row (visually 4 vertically).
    for r in range(len(board)):
        for c in range(len(board[r])-3):
            if same_pieces(board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]):
                board[r][c] = 0
                board[r][c+1] = 0
                board[r][c+2] = 0
                board[r][c+3] = 0
                turn_score += 4
    # 4 vertically in  row (visually 4 horizontally).
    for r in range(len(board)-3):
        for c in range(len(board[r])):
            if same_pieces(board[r][c], board[r+1][c], board[r+2][c], board[r+3][c]):
                board[r][c] = 0
                board[r+1][c] = 0
                board[r+2][c] = 0
                board[r+3][c] = 0
                turn_score += 4
    # 3 Horizontal in a row (visually 3 vertically).
    for r in range(len(board)):
        for c in range(len(board[r])-2):
            if same_pieces(board[r][c], board[r][c+1], board[r][c+2]):
                board[r][c] = 0
                board[r][c+1] = 0
                board[r][c+2] = 0
                turn_score += 3
    # 3 Vertical in a row (visually 3 horizontal).
    for r in range(len(board)-2):
        for c in range(len(board[r])):
            if same_pieces(board[r][c], board[r+1][c], board[r+2][c]):
                board[r][c] = 0
                board[r+1][c] = 0
                board[r+2][c] = 0
                turn_score += 3
    # If the score that turn is higher than one match of 3, multiply by 1.5 as combo bonus.
    if turn_score > 3 and multiplier is not None:
        return turn_score * 100 * multiplier, False
    elif turn_score > 0:
        return turn_score * 100, False
    else:
        return 0, True


def vert_line(board, r, c):
    """
    Check a given position on a 2D array for a vertical line of 3 pieces that are the same, whether it be the top,
    middle or bottom of the three.
    :param board: The 2D array representing the current game board or pieces.
    :param r: The row in the array of the piece being tested.
    :param c: The column in the array of the piece being tested.
    :return: True, if a line of three has been found. False, otherwise.
    """
    if r+1 in range(len(board)) and r-1 in range(len(board)):
        if board[r][c] == board[r+1][c] == board[r-1][c]:
            return True
    if r+1 in range(len(board)) and r+2 in range(len(board)):
        if board[r][c] == board[r+1][c] == board[r+2][c]:
            return True
    if r-1 in range(len(board)) and r-2 in range(len(board)):
        if board[r][c] == board[r-2][c] == board[r-1][c]:
            return True
    # Return False if all tests fail.
    return False


def horz_line(board, r, c):
    """
    Checks if a certain game piece is part of a horizontal line of three pieces that are the same, whether it be
    the farthest left, middle of farthest right piece in the row of three.
    :param board: The 2D array representing the current board of pieces.
    :param r: The row of the specific piece being tested.
    :param c: The column of the specific piece being tested.
    :return: True, if the particular piece makes a row of three. False, otherwise.
    """
    if c-1 in range(len(board[0])) and c+1 in range(len(board[0])):
        if board[r][c] == board[r][c-1] == board[r][c+1]:
            return True
    if c+1 in range(len(board[0])) and c+2 in range(len(board[0])):
        if board[r][c] == board[r][c+1] == board[r][c+2]:
            return True
    if c-1 in range(len(board[r])) and c-2 in range(len(board[0])):
        if board[r][c] == board[r][c-1] == board[r][c-2]:
            return True
    # Return False if all tests fail.
    return False


def moves_left(board, turns, score, target):
    """
    Checks if there are any remaining moves which are valid.
    :param board: Game board array (2D).
    :param turns: Amount of turns left.
    :param score: Current Score.
    :param target: Target score for the player.
    :return: True, if a move is found. False, otherwise.
    """
    for r in range(len(board)):
        for c in range(1, len(board[r])):
            if r+1 in range(len(board)):
                if valid_swap(board, r, c, r+1, c):
                    tTG.swap_animation(turns, score, target, board, r, c, r+1, c)
                    swap(board, r, c, r+1, c)
                    return True
            if c+1 in range(len(board[0])):
                if valid_swap(board, r, c, r, c+1):
                    tTG.swap_animation(turns, score, target, board, r, c, r, c+1)
                    swap(board, r, c, r, c+1)
                    return True
            if r-1 in range(len(board)):
                if valid_swap(board, r, c, r-1, c):
                    tTG.swap_animation(turns, score, target, board, r, c, r-1, c)
                    swap(board, r, c, r-1, c)
                    return True
            if c-1 in range(len(board[0])):
                if valid_swap(board, r, c, r, c-1):
                    tTG.swap_animation(turns, score, target, board, r, c, r, c-1)
                    swap(board, r, c, r, c-1)
                    return True
    return False


def valid_swap(board, r1, c1, r2, c2):
    """
    Checks a particular move when made to see if it completes a vertical or horizontal line of three of the same piece.
    :param board: The 2D array representing the current game board.
    :param r1: The row of the first piece selected.
    :param c1: The column of the first piece selected.
    :param r2: The row of the second piece selected.
    :param c2: The column of the second piece selected.
    :return: True, if the swap resulted in a match of three. False, otherwise.
    """
    # Initially swap the given pieces
    swap(board, r1, c1, r2, c2)
    if horz_line(board, r1, c1) or horz_line(board, r2, c2) or vert_line(board, r1, c1) or vert_line(board, r2, c2):
        # Swap pieces back to there original location
        swap(board, r1, c1, r2, c2)
        return True
    # Swap pieces back to their original places
    else:
        swap(board, r1, c1, r2, c2)
        # Return that no swap can be made
        return False


def drop_swap(board, max_piece):
    """
    This function deletes all occurrences of no game pieces (0 in the array) and each time replaces such occurrence with
    a new random piece.
    :param board: The 2D array representing the current game board.
    :param max_piece: The integer representing the amount of unique game pieces to be randomly selected from.
    :return: True, if the function deleted any non occurrences when called. False, if no zeros were found.
    """
    zero_count = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                del board[r][c]
                board[r].append(random.randint(1, max_piece))
                zero_count += 1

    return zero_count > 0


def play_game(game_board, turns_left, target_score, max_piece, multiplier):
    score = 0
    good_board = True
    while turns_left != 0 and good_board:
        tTG.set_constants(turns_left, score, target_score)
        tTG.draw_board(game_board)
        # Before first turn, delay for one second so viewer can see initial board.
        if turns_left == 30 or turns_left == 35:
            time.sleep(1.25)
        good_board = moves_left(game_board, turns_left, score, target_score)
        score += clear_matches(game_board, multiplier)[0]
        turns_left -= 1
        cleared = False
        time.sleep(0.1)
        while not cleared:
            dropping = True
            while dropping:
                tTG.clear()
                tTG.set_constants(turns_left, score, target_score)
                tTG.draw_board(game_board)
                time.sleep(0.2)
                dropping = drop_swap(game_board, max_piece)
            result = clear_matches(game_board, multiplier)
            time.sleep(0.2)
            tTG.clear()
            tTG.set_constants(turns_left, score, target_score)
            tTG.draw_board(game_board)
            score += result[0] * multiplier
            cleared = result[1]
    possible_moves = turns_left == 0
    tTG.set_constants(turns_left, score, target_score)
    tTG.draw_board(game_board)
    tTG.show(1250)
    # Display GAME OVER screen
    tTG.play_again(turns_left, score, target_score, possible_moves)


def main():

    while True:
        difficulty = tTG.start_screen()
        # Easy selected.
        if difficulty == "easy":
            win_score = 20000  # max_score: the target score for the user to attain.
            max_turns = 30  # max_turns: user turn allotment.
            piece_num = 6
            bonus_match_multiplier = 1.3
        # Hard selected.
        else:
            win_score = 25000
            max_turns = 35
            piece_num = 7
            bonus_match_multiplier = 1.6
        start_board = make_board(piece_num)
        play_game(start_board, max_turns, win_score, piece_num, bonus_match_multiplier)


if __name__ == "__main__":
    main()
