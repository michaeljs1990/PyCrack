#custom libs
import crack
import prehashedcrack


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


""" This checked the hashes input against a pre defined hash list.
We do not check for hash type as we expect the user to be using the
right hashes if they have computed a pre defined list."""
def prehashedcrack(hashx, sharedCount, sharedPass):
    word = hashx.rstrip('\n')
    #set to allow user to select list later
    hashlist = open('lists/test.txt')
    prehashedcrack.crack(word, hashlist, sharedCount, sharedPass)
