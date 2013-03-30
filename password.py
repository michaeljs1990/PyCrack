#custom lib
import crack


""" This module is used to get the hash from config/dictionary.txt
and then evaluate what kind of hash it is. sharedCount and sharedPass
use the multiprocessing.Value() function."""
def crackhash(hashx, sharedCount, sharedPass):
    word = hashx.rstrip('\n')
    dictionary = open('config/dictionary.txt', 'r+')
    if '$6$' in word:
        crack.nixSha512(word, dictionary, sharedCount, sharedPass)
    if '$2a$12$' in word:
        crack.nixBlowfish(word, dictionary, sharedCount, sharedPass)
    if '$sha$' in word:
        crack.hashsha(word, dictionary, sharedCount, sharedPass)
    if '$md5$' in word:
        crack.hashmd5(word, dictionary, sharedCount, sharedPass)


#def prehashedlookup()
"""this function will take a list that has been pre-hashed and run through the currently loaded hash"""
