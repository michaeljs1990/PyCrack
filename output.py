import curses
import time
import multiprocessing
import Queue

#custom imports
import password

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

def printRight(window, uinput, row, number):
    winTopRight = window[1]
    #if row > 18:
    #    row = 1
    time_sleep = 3
    hash_per_second = str((uinput/time_sleep) / number) + ' h/s'
    uinput = str(uinput) + ' hash'
    winTopRight.addstr(row , 1, uinput + '\t' + hash_per_second)
    winTopRight.refresh()
    return (number + 1)
    
    
if __name__ == "__main__":
    window = interface()
    
    #Print to left screen
    hashfile = open('config/cracklistB.txt', 'r+')
    row = 1
    for hashx in hashfile:
        if hashx[0] != '#':
            row = printLeft(window, hashx, row)
    
    #print to right screen
    hashfile.seek(0,0)
    row = 1
    number = 1
    for hashx in hashfile:
        if hashx[0] != '#':
            #shared is a variable that both procs can access
            shared = multiprocessing.Value('i', 0)
            proc = multiprocessing.Process(
                    target = password.crackhash,
                    args = (hashx, shared))
            proc.start()
            while proc.is_alive():
                number = printRight(window, shared.value, row, number)
                time.sleep(3)
    
    #Clean exit from curses GUI
    curses.endwin()
