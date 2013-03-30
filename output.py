import curses
import time
import multiprocessing

#custom imports
import password
import listhash


""" Creates a curses window object and two windows
on the right and left side."""
def interface():
        screen = curses.initscr()
        screenSize = screen.getmaxyx()
        screen.addstr(0, 1, 'PyMon Version 0.1dev')
        botInput = curses.newwin(3, 102, 21, 0)
        winTopLeft = curses.newwin(20, 50, 1, 0)
        winTopRight = curses.newwin(20, 50, 1, 52)
        winTopLeft.border()
        winTopRight.border()
        botInput.border()
        screen.refresh()
        winTopLeft.refresh()
        winTopRight.refresh()
        botInput.refresh()
        return winTopLeft, winTopRight, botInput


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
    time_sleep = 2
    hash_per_second = str((count/time_sleep) / number) + ' h/s'
    count = str(count) + ' hash'
    winTopRight.addstr(row , 1, count + '\t' + hash_per_second + '\t ' + password)
    winTopRight.refresh()
    return (number + 1)

""" Options available when starting the program"""
def mainMenu(winTopLeft, winTopRight, botInput):
    winTopRight.clear()
    winTopRight.border()
    winTopRight.refresh()
    winTopLeft.clear()
    winTopLeft.border()
    winTopLeft.addstr(1, 1, 'Main Menu Options')
    winTopLeft.addstr(3, 1, 'hash -- start hashing')
    winTopLeft.addstr(4, 1, 'hashlist -- make hash list')
    winTopLeft.addstr(5, 1, 'loaddict -- load new dictionary')
    winTopLeft.addstr(6, 1, 'loadhash -- load new hash list')
    winTopLeft.refresh()
    cmd = botInput.getstr(1, 2)
    winTopLeft.clear()
    winTopLeft.border()
    botInput.clear()
    botInput.border()
    botInput.refresh()
    winTopLeft.refresh()
    return cmd

""" This promps the user for all information needed to
make a hash list from a given dictionary."""
def hashListGetInput(winTopLeft, winTopRight, botInput):
    winTopLeft.clear()
    winTopLeft.border()
    winTopLeft.addstr(1, 1, 'Enter the name for your list.')
    winTopLeft.addstr(2, 1, 'It will be put in the lists directory.')
    winTopLeft.refresh()
    listName = botInput.getstr(1, 2)
    botInput.clear()
    botInput.border()
    botInput.refresh()
    winTopLeft.clear()
    winTopLeft.border()
    winTopLeft.addstr(1, 1, 'Enter one of the following hash types.')
    winTopLeft.addstr(4, 1, '> nixSha512')
    winTopLeft.addstr(5, 1, '> nixBlowfish')
    winTopLeft.addstr(6, 1, '> sha1')
    winTopLeft.addstr(7, 1, '> sha224')
    winTopLeft.addstr(8, 1, '> sha256')
    winTopLeft.addstr(9, 1, '> sha384')
    winTopLeft.addstr(10, 1, '> sha512')
    winTopLeft.addstr(11, 1, '> md5')
    winTopLeft.refresh()
    listType = botInput.getstr(1, 2)
    botInput.clear()
    botInput.border()
    botInput.refresh()
    winTopLeft.clear()
    winTopLeft.border()
    winTopLeft.addstr(1, 1, 'Enter the salt to be used.')
    winTopLeft.refresh()
    listSalt = botInput.getstr(1, 2)
    botInput.clear()
    botInput.border()
    botInput.refresh()
    return listName, listType, listSalt
    

""" Main function to start the entire hashing process.
sharedCount and sharedPass are used to keep track of
how many hashs have been checked and how fast."""    
if __name__ == "__main__":
    window = interface()
    winTopLeft = window[0]
    winTopRight = window[1]
    botInput = window[2]
    
    cmd = 'run'

    while cmd != 'exit' and cmd != 'quit':
        cmd = mainMenu(winTopLeft, winTopRight, botInput)
        #hash strings from cracklist.txt
        if cmd == 'hash' or cmd == 'hx':
            #left screen
            hashfile = open('config/cracklist.txt', 'r+')
            row = 1
            for hashx in hashfile:
                if hashx[0] != '#':
                    row = printLeft(window, hashx, row)
            #right screen
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
                        time.sleep(2)
                    printRight(window, sharedCount.value,
                               sharedPass.value, row, number)
                    row = row + 1
        if cmd == 'hashlist':
            dictionary = open('config/dictionary.txt')
            listName, listType, listSalt = hashListGetInput(winTopLeft, winTopRight, botInput)
            listhash.makeHashList(listName, listType, dictionary, listSalt)
        if cmd == 'loaddict':
            pass
        if cmd == 'loadhash':
            pass

    curses.endwin()
