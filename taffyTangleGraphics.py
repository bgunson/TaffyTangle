"""
My graphics module for my version of Taffy Tangle for CPSC 231, Assignment 5 Problem 2, Fall 2018.
Utilizes the external stddraw module.

Bennett Gunson
November 20, 2018

"""


from stddraw import *


def set_constants(turns, score, target_score):
    """
    Draw/set the constant aspects and visuals of the game to the window when called including setting the x/y scales,
    clear the board with book red background, draw the title, and draw the playing surface.
    """
    setXscale(-2, 9)
    setYscale(-2, 11)
    clear(BOOK_RED)
    setPenColor(PINK)
    setFontFamily("algerian")
    setFontSize(60)
    text(3.5, 10, "TAFFY TANGLE")
    # Playing surface.
    setPenColor(LIGHT_GRAY)
    filledRectangle(-0.25, -0.25, 7.5, 9.5)
    setPenColor()
    setPenRadius(0.01)
    rectangle(-0.25, -0.25, 7.5, 9.5)
    display_stats(turns, score, target_score)


def display_stats(turns, score, target_score):
    """
    Display the turns left, the players current score and target score at the moment of being called.
    """
    setPenRadius(0.004)
    setPenColor(WHITE)
    filledRectangle(-0.25, -2, 7.5, 1.5)
    setPenColor()
    rectangle(-0.25, -2, 7.5, 1.5)
    setFontFamily("arial")
    setFontSize(20)
    setPenColor()
    text(3.5, -1, "Turns Left:")
    text(3.5, -1.5, "{}".format(turns))
    text(1, -1, "Score:")
    text(1, -1.5, "{}".format(int(score)))
    text(6, -1, "Target Score:")
    text(6, -1.5, "{}".format(target_score))
    # Hint Button
    setPenColor(YELLOW)
    filledSquare(-1, -1, 0.5)
    setPenColor()
    square(-1, -1, 0.5)
    setFontFamily("goudy stout")
    setFontSize(9)
    text(-1, -1, "HINT")


def draw_board(current_board):
    """
    Iterate through the current board 2D array and display the piece to the window.
    """
    for i in range(len(current_board)):
        for j in range(len(current_board[i])):
            if current_board[i][j] != 0:
                draw_piece(current_board[i][j], i, j)
    show(0)


def start_end_frame(colour_count):
    """
    The pen colour setter that based on an incrementing colour count which is passed via parameter followed by drawing
    the coloured frame to the window.
    """
    if colour_count == 1:
        setPenColor(RED)
    elif colour_count == 2:
        setPenColor(BLUE)
    elif colour_count == 3:
        setPenColor(ORANGE)
    elif colour_count == 4:
        setPenColor(GREEN)
    elif colour_count == 5:
        setPenColor(MAGENTA)
    elif colour_count == 6:
        setPenColor(CYAN)
    else:
        setPenColor(WHITE)
    filledRectangle(-0.25, -0.25, 7.5, 9.5)
    setPenColor(PINK)
    filledRectangle(0.5, 0.5, 6, 8)
    setPenColor()
    setPenRadius(0.01)
    rectangle(0.5, 0.5, 6, 8)
    rectangle(-0.25, -0.25, 7.5, 9.5)


def start_screen():
    """
    The start screen animation/menu screen.
    """
    set_constants(0, 0, 0)
    clear(BOOK_RED)
    good = False
    while not good:
        colour_count = 1
        while not mousePressed():
            start_end_frame(colour_count)
            button("easy")
            button("hard")
            setFontSize(28)
            setFontFamily("goudy stout")
            text(3.5, 7.5, "WELCOME")
            setFontSize(18)
            text(3.5, 6.6, "TO")
            setFontSize(36)
            setFontFamily("algerian")
            text(3.5, 5.5, "TAFFY TANGLE")
            setFontSize(18)
            setFontFamily("arial")
            # Draw the shapes across screen.
            x = 0.55
            for i in range(1, 8):
                draw_piece(i, x, 4)
                x += 0.8125
            # Show each cycle for one second then change the colour of the start/end frame via colour counter.
            show(1000)
            colour_count += 1
            if colour_count == 8:
                colour_count = 1
        # Check if user click was on a button and return the difficulty accordingly.
        mx, my = mouseX(), mouseY()
        if 2 <= int(mx) < 5 and 2 <= int(my) < 3:
            return "easy"
        if 2 <= int(mx) < 5 and 1 <= int(my) < 2:
            return "hard"


def game_over(turns, score, target, colour_count, more_moves):
    """
    Show the end screen after a game has ended, show win/loss
    """
    clear(BOOK_RED)
    start_end_frame(colour_count)
    setFontSize(40)
    setFontFamily("algerian")
    text(3.5, 5.5, "GAME OVER")
    setPenColor(PINK)
    setFontFamily("algerian")
    setFontSize(60)
    text(3.5, 10, "TAFFY TANGLE")
    button("play again")
    setFontSize(24)
    setPenColor()
    setFontFamily("arial")
    if not more_moves and score < target:
        text(3.5, 4.5, "No more possible moves...")
    elif turns == 0 and score < target:
        setFontFamily("goudy stout")
        text(3.5, 4.5, "LOSER!")
        setFontFamily("arial")
        text(3.5, 3.5, "You ran out of turns!")
    elif not more_moves and score >= target:
        setFontFamily("goudy stout")
        text(3.5, 4.5, "WINNER!")
        setFontFamily("arial")
        text(3.5, 3.5, "No more possible moves...")
    elif score > target:
        setFontFamily("goudy stout")
        text(3.5, 4.5, "WINNER!")
    setFontFamily("arial")
    setFontSize(22)
    total_score = "Total Score: " + str(int(score))
    text(3.5, 1.5, "{}".format(total_score))
    setFontSize(16)
    target_score = "Target Score: " + str(target)
    text(3.5, 1, target_score)

    show(1000)


def button(button_type):
    """
    Function draws a particular type of button when called with the type of button as parameter.
    :param button_type: The string passed representing what type of button is desired elsewhere in program.
    Three locations on the window (Hard, Easy/Play Again), with labels (Hard, Easy and Play Again).
    :return:
    """
    setPenColor()
    setFontSize(20)
    setFontFamily("goudy stout")
    if button_type == "easy":
        setPenColor(YELLOW)
        filledRectangle(2, 2, 3, 1)
        setPenColor()
        setPenRadius(0.005)
        rectangle(2, 2, 3, 1)
        text(3.5, 2.5, "EASY")
    elif button_type == 'hard':
        setPenColor(YELLOW)
        filledRectangle(2, 1, 3, 1)
        setPenColor()
        setPenRadius(0.005)
        rectangle(2, 1, 3, 1)
        setPenColor()
        text(3.5, 1.5, "HARD")
    elif button_type == "play again":
        setPenColor(YELLOW)
        filledRectangle(2, 2, 3, 1)
        setPenColor()
        setPenRadius(0.005)
        rectangle(2, 2, 3, 1)
        setPenColor()
        setFontSize()
        text(3.5, 2.5, "PLAY AGAIN")


def play_again(turns, score, target, more_moves):
    """
    A visual display that draws the game over screen until the user hits 'play again' button.
    :param turns: The amount of turns left in the game when it ended.
    :param score: The final ending score of the player.
    :param target: The target score of the game depending on difficulty.
    :param more_moves: Either True or False, if the game ended with or without more possible moves.
    """
    good = False
    while not good:
        colour_count = 1
        while not mousePressed():
            game_over(turns, score, target, colour_count, more_moves)
            # Create an incrementing counter as the loop cycles to alternate the colour of the frame for animation.
            colour_count += 1
            # Reset the counter is it maxes out past the predefined corresponding colour number.
            if colour_count == 8:
                colour_count = 1
        mx, my = mouseX(), mouseY()
        # If players click was on 'play again' button end the loop.
        if 2 <= int(mx) < 5 and 2 <= int(my) < 3:
            good = True


def show_hint(location):
    """
    Draw the hint on the board window for one second.
    :param location: A for value list that represents the hint location in form [row_1, col_1, row_2, col_2].
    """
    time.sleep(0.2)
    setPenColor(DARK_GREEN)
    square(location[0]+0.5, location[1]+0.5, 0.5)
    square(location[2]+0.5, location[3]+0.5, 0.5)
    show(1000)


def selection(hint):
    """
    This function waits for user input with in the game board in the window whilst drawing the board and ultimately
    returns the integer positions of the mouse click which correspond with the indexes of the 2D array.
    :param hint: If the user presses the hint button, it calls the show_hint function.
    """
    while True:
        show(0)
        if mousePressed():
            mx = mouseX()
            my = mouseY()
            if -1.5 <= mx < -0.5 and -1.5 <= my < -0.5:
                show_hint(hint)
                return -1, -1
            elif 0 <= mx <= 7 and 0 <= my <= 9:
                mx = int(mx)
                my = int(my)
                setPenColor(YELLOW)
                rectangle(mx, my, 1, 1)
                return mx, my
            else:
                # If click was off the board return a redundant non piece location to cancel the turn.
                return -1, -1


def swap_animation(turns, score, target_score, board, r1, c1, r2, c2):
    """
    Function swaps two user chosen pieces visually on the current game board, displaying in minuscule increments in
    order to show smooth movement. We can assume are adjacent when they are passed after that condition
    was checked before calling this function.

    """
    # Assign temporary placeholders as the original indexes and value in the board will be altered.
    piece_1 = board[r1][c1]
    piece_2 = board[r2][c2]
    temp_r1, temp_c1, temp_r2, temp_c2 = r1, c1, r2, c2
    swapped = False
    # Make the pieces in question 0 so nothing is drawn while the swap is drawing the temp. 'moving' pieces.
    board[r1][c1] = 0
    board[r2][c2] = 0
    # If the swap is being made within the same row.
    if r1 == r2:
        col_diff = c2 - c1
        while not swapped:
            clear(BOOK_RED)
            set_constants(turns, score, target_score)
            draw_board(board)
            draw_piece(piece_1, temp_r1, temp_c1)
            draw_piece(piece_2, temp_r2, temp_c2)
            # Increment the pieces' movement.
            temp_c1 += 0.04 * col_diff
            temp_c2 -= 0.04 * col_diff
            # Check that the temp pieces are not within 0.01 of the others original position, if so the loop will break.
            swapped = abs(temp_c1 - c2) < 0.01 and abs(temp_c2 - c1) < 0.01
            show(0)
    # If the swap is being made within the same column; follow the same actions above but within the column.
    else:
        row_diff = r2 - r1
        while not swapped:
            clear(BOOK_RED)
            set_constants(turns, score, target_score)
            draw_board(board)
            draw_piece(piece_1, temp_r1, temp_c1)
            draw_piece(piece_2, temp_r2, temp_c2)
            temp_r1 += 0.04 * row_diff
            temp_r2 -= 0.04 * row_diff
            swapped = abs(temp_r1 - r2) < 0.01 and abs(temp_r2 - r1) < 0.01
            show(0)
    # Reset the game pieces to their original piece.
    board[r1][c1] = piece_1
    board[r2][c2] = piece_2


def draw_piece(num, x, y):
    """
    This function is able to physically draw 7 distinct shapes to the window when called. If a number out of the
    range is passed, the function does no actions.
    """
    # Centre the coordinates of the shape to the centre of its grid location.
    x += 0.5
    y += 0.5
    setPenRadius(0.0029)
    if num == 1:    # Function calls for shape one, red circle.
        setPenColor(RED)
        filledCircle(x, y, 0.375)
        setPenColor()
        circle(x, y, 0.375)

    elif num == 2:  # Function calls for shape two, blue square.
        setPenColor(BLUE)
        filledSquare(x, y, 0.3)
        setPenColor()
        square(x, y, 0.3)

    elif num == 3:  # Function calls for shape three, orange triangle.
        setPenColor(ORANGE)
        filledPolygon([x+0.3, x, x-0.3], [y-0.3, y+0.3, y-0.3])
        setPenColor()
        polygon([x+0.3, x, x-0.3], [y-0.3, y+0.3, y-0.3])

    elif num == 4:  # Function calls for shape four, green diamond
        setPenColor(GREEN)
        filledPolygon([x, x+0.35, x, x-0.35], [y+0.3, y, y-0.3, y])
        setPenColor()
        polygon([x, x+0.35, x, x-0.35], [y+0.3, y, y-0.3, y])

    elif num == 5:  # Function calls for shape five, Magenta pointy thing.
        setPenColor(MAGENTA)
        filledPolygon([x+0.3, x-0.3, x-0.15, x+0.3], [y+0.15, y+0.3, y-0.3, y-0.3])
        setPenColor()
        polygon([x+0.3, x-0.3, x-0.15, x+0.3], [y+0.15, y+0.3, y-0.3, y-0.3])

    elif num == 6:  # Function calls for shape six, cyan bow-tie thing.
        setPenColor(CYAN)
        filledPolygon([x+0.3, x+0.15, x-0.15, x-0.3, x-0.15, x+0.15],
                      [y, y+0.3, y+0.3, y, y-0.3, y-0.3])
        setPenColor()
        polygon([x+0.3, x+0.15, x-0.15, x-0.3, x-0.15, x+0.15],
                [y, y+0.3, y+0.3, y, y-0.3, y-0.3])
    elif num == 7:
        setPenColor(WHITE)
        filledPolygon([x+0.35, x+0.15, x+0.15, x-0.15, x-0.15, x-0.35, x-0.35, x-0.15, x-0.15, x+0.15, x+0.15, x+0.35],
                      [y+0.15, y+0.15, y+0.35, y+0.35, y+0.15, y+0.15, y-0.15, y-0.15, y-0.35, y-0.35, y-0.15, y-0.15])
        setPenColor()
        polygon([x+0.35, x+0.15, x+0.15, x-0.15, x-0.15, x-0.35, x-0.35, x-0.15, x-0.15, x+0.15, x+0.15, x+0.35],
                [y+0.15, y+0.15, y+0.35, y+0.35, y+0.15, y+0.15, y-0.15, y-0.15, y-0.35, y-0.35, y-0.15, y-0.15])
    else:
        # Draw nothing.
        pass
