#Looks in password.txt for passwords and evaluates the function
#that should be called to crack it.
import crack


dictionary = open('config/dictionary.txt', 'r+')


def crackhash(hashx, sharedCount, sharedPass):
        word = hashx.rstrip('\n')
        if '$6$' in word:
            crack.nixSha512(word, dictionary, sharedCount, sharedPass)
        if '$2a$12$' in word:
            crack.nixBlowfish(word, dictionary, sharedCount, sharedPass)
