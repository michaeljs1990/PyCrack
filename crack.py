#crypto libs
import hashlib
import crypt
import bcrypt
import time


""" Takes in hashx from nixSha512
and outputs it in two words. """
def nixSha512Sort(word):
    word = word.split('$')
    salt = '$' + word[1] + '$' + word[2] + '$'
    password = word[3].split(':')[0]
    return salt, password


""" Takes in formated hash from cracklist.txt and splits
it into a usable salt and hash. The loop then pulls in a word
from dictionary.txt and hashs it to check against your hash. """
def nixSha512(hashx, dictionary, sharedCount, sharedPass):
    salt, password = nixSha512Sort(hashx)
    for word in dictionary:
        word = word.rstrip()
        sharedCount.value = sharedCount.value + 1
        if crypt.crypt(word, salt) == (salt + password):
            sharedPass.value = word
            break


""" Takes in hashx from nixBlowfish
and outputs it in two words. """
def nixBlowfishSort(word):
    salt = word[:29]
    password = word[29:]
    return salt, password


""" Takes in hashx from cracklist.txt and calls nixBlowfishSort
to generate a salt and password. It then goes through dictionary.txt
and hashs each word to test against the input salt and password. """
def nixBlowfish(hashx, dictionary, sharedCount, sharedPass):
    salt, password = nixBlowfishSort(hashx)
    for word in dictionary:
        word = word.rstrip()
        sharedCount.value = sharedCount.value + 1
        if bcrypt.hashpw(word, salt) == (salt + password):
            sharedPass.value = word
            break

def hashsha1sort(word):
    word = word.split('$')
    salt = word[2]
    password = word[3]
    return salt, password


def hashsha1(hashx, dictionary, sharedCount, sharedPass):
    salt, password = hashsha1sort(hashx)
    for word in dictionary:
        word = word.rstrip()
        sharedCount.value = sharedCount.value + 1
        if hashlib.sha1(salt + word) == password:
            sharedPass.value = word
            break
