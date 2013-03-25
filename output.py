import curses
import time
import multiprocessing

#custom imports
import password


""" Creates a curses window object and two windows
on the right and left side."""
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


""" Prints out input to the left screen. set 
row = printLeft() when using and place inside
a loop for input to print out input and go to next row. """
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

""" Print out input to right screen. This is used to display
all information about the current process. must return to 
number = printRight() in order for hash_per_second to calculate
properly."""
def printRight(window, count, password, row, number):
    winTopRight = window[1]
    time_sleep = 3
    hash_per_second = str((count/time_sleep) / number) + ' h/s'
    count = str(count) + ' hash'
    winTopRight.addstr(row , 1, count + '\t' + hash_per_second + '\t ' + password)
    winTopRight.refresh()
    return (number + 1)


""" Main function to start the entire hashing process.
sharedCount and sharedPass are used to keep track of
how many hashs have been checked and how fast."""    
if __name__ == "__main__":
    window = interface()
    
    hashfile = open('config/cracklist.txt', 'r+')
    row = 1
    for hashx in hashfile:
        if hashx[0] != '#':
            row = printLeft(window, hashx, row)
    
    hashfile.seek(0,0)
    row = 1
    for hashx in hashfile:
        if hashx[0] != '#':
            number = 1
            sharedCount = multiprocessing.Manager().Value('i', 0)
            sharedPass = multiprocessing.Manager().Value(unicode, 'Nope')
            proc = multiprocessing.Process(
                    target = password.crackhash,
                    args = (hashx, sharedCount, sharedPass))
            proc.start()
            while proc.is_alive():
                number = printRight(window, sharedCount.value,
                          sharedPass.value, row, number)
                time.sleep(3)
            printRight(window, sharedCount.value,
             sharedPass.value, row, number)
            row = row + 1
    
    curses.endwin()
