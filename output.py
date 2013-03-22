import curses
import time
import multiprocessing

#custom imports
import password
import crack

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

def printLeft(window, uinput, row):
    winTopLeft = window[0]
    if row > 18:
        row = 1
    uinput = str(uinput)
    if len(uinput) > 48:
        uinput = uinput[:45] + '...'
    winTopLeft.addstr(row, 1, uinput)
    winTopLeft.refresh()
    return row + 1

def printRight(window, uinput , row):
    winTopRight = window[1]
    #if row > 18:
    #    row = 1
    winTopRight.addstr(row , 1, uinput)
    winTopRight.refresh()
    #return row + 1
    
    
if __name__ == "__main__":
    window = interface()
    
    #Print to left screen
    hashfile = open('config/cracklistB.txt', 'r+')
    row = 1
    for hashx in hashfile:
        if hashx[0] != '#':
            row = printLeft(window, hashx, row)
    
    #print to right screen
    hashfile = open('config/cracklistB.txt', 'r+')
    row = 1
    for hashx in hashfile:
        if hashx[0] != '#':
            #shared is a variable that both procs can access
	    svar = 0
            shared = multiprocessing.Value('d', svar)
            proc = multiprocessing.Process(
                    target = password.crackhash,
                    args = (hashx, shared))
            proc.start()
            while True:
                printRight(window, str(shared.value), row)
                time.sleep(5)
    #Clean exit from curses GUI
    curses.endwin()
