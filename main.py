import curses

board = [*" b b b bb b b b  b b b b' ' ' '  ' ' ' 'a a a a  a a a aa a a a "]
cursorPosition = 34

def getDirection(key):
    if   key == 452 or key == 97: key = "left"
    elif key == 450 or key == 119: key = "up"
    elif key == 456 or key == 115: key = "down"
    elif key == 454 or key == 100: key = "right"
    return key

def getPosition(position, key):
    if key == "left":  position -= 1
    if key == "right": position += 1
    if key == "up":    position -= 8
    if key == "down":  position += 8
    return position

def getFrame(position, board):
    frame = []
    for i in range(len(board)):
        if i != position:
            if i % 8 == 0 and i != 0: frame.append("\n")
            frame.append(board[i])
        else:
            if i % 8 != 0 or i == 0: frame.append("$")
            else: frame.append("\n$")
    return frame

def getMoves(position, board):
    if board[position] == "a":
        pass
    elif board[position] == "b":
        pass

screen = curses.initscr()
screen.keypad(True)
while True:
    boardFrame = getFrame(cursorPosition, board)

    screen.clear()
    screen.addstr("".join(boardFrame))
    screen.addstr("\n\n"+str(cursorPosition))

    key = getDirection(screen.getch())
    if key == 27 or key == 113: break
    cursorPosition = getPosition(cursorPosition, key)

curses.endwin()