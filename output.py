import curses
import time

#note when calling screen in printLeft() or printRight()
#you must make sure to pay attention to the order 
#windows are returned in.
def interface():
        screen = curses.initscr()
        screenSize = screen.getmaxyx()
        screen.addstr(0, 1, 'PyMon Version 0.1dev')
        winTopLeft = curses.newwin(20, 50, 1, 0)
        winTopRight = curses.newwin(20, 50, 1, 52)
        winTopLeft.border()
        winTopRight.border()
        screen.refresh()
        winTopLeft.refresh()
        winTopRight.refresh()
        return winTopLeft, winTopRight

def printLeft(window, input, row):
    winTopLeft = window[0]
    if row > 18:
        row = 1
    input = str(input)
    loc = winTopLeft.getparyx()
    winTopLeft.addstr(row,1, input)
    winTopLeft.refresh()
    return row + 1

#def printRight(window[1], input):
#    input = str(input)
#    loc = winTopRight.getparyx()
#    winTopRight.addstr(1,1, input)
#    winTopRight.refresh()
    
    

window = interface()
x, row = 0, 1
while x < 20:
    row = printLeft(window, 'Hey I hope this works', row)
    time.sleep(1)
    x = x + 1

curses.endwin()
