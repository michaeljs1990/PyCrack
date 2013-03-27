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


""" Takes in hash from sha1 and
breaks it into a salt and password."""
def hashShaSort(word):
    word = word.split('$')
    shatype = word[2]
    salt = word[3]
    password = word[4]
    return shatype, salt, password


""" Reads in word off of cracklist.txt and calls hashsha1sort
to break it into usable pieces. It then goes and checks the
hash against each word in dictionary.txt this processes all
non unix sha hashes. (1, 224, 256, 384, and 512)"""
def hashsha(hashx, dictionary, sharedCount, sharedPass):
    shatype, salt, password = hashShaSort(hashx)
    if shatype == '1':
        for word in dictionary:
            word = word.rstrip()
            sharedCount.value = sharedCount.value + 1
            if hashlib.sha1(salt + word).hexdigest() == password:
                sharedPass.value = word
                break
    if shatype == '224':
        for word in dictionary:
            word = word.rstrip()
            sharedCount.value = sharedCount.value + 1
            if hashlib.sha224(salt + word).hexdigest() == password:
                sharedPass.value = word
                break
    if shatype == '256':
        for word in dictionary:
            word = word.rstrip()
            sharedCount.value = sharedCount.value + 1
            if hashlib.sha256(salt + word).hexdigest() == password:
                sharedPass.value = word
                break
    if shatype == '384':
        for word in dictionary:
            word = word.rstrip()
            sharedCount.value = sharedCount.value + 1
            if hashlib.sha384(salt + word).hexdigest() == password:
                sharedPass.value = word
                break
    if shatype == '512':
        for word in dictionary:
            word = word.rstrip()
            sharedCount.value = sharedCount.value + 1
            if hashlib.sha512(salt + word).hexdigest() == password:
                sharedPass.value = word
                break


"""MD5 Sort"""
def hashSortMd5(word):
    word = word.split('$')
    salt = word[2]
    password = word[3]
    return salt, password


"""MD5 hash"""
def hashmd5(hashx, dictionary, sharedCount, sharedPass):
    salt, password = hashSortMd5(hashx)
    for word in dictionary:
        word = word.rstrip()
        sharedCount.value = sharedCount.value + 1
        if hashlib.md5(salt + word).hexdigest() == password:
            sharedPass.value = word
            break
