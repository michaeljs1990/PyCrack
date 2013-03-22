#crypto libs
import hashlib
import crypt
import bcrypt
import datetime


#sorts the nixPwd hash
def nixSha512Sort(word):
    word = word.split('$')
    salt = '$' + word[1] + '$' + word[2] + '$'
    password = word[3].split(':')[0]
    return salt, password

#cracks the sha512 unix hash
def nixSha512(hashx, dictionary, shared):
    salt, password = nixSha512Sort(hashx)
    a = datetime.datetime.now()
    for word in dictionary:
        word = word.rstrip()
        shared.value = shared.value + 1
        if crypt.crypt(word, salt) == (salt + password):
            time = datetime.datetime.now() - a
            return word

#sorts blowfish hashs for use in nixBlowfish
def nixBlowfishSort(word):
    salt = word[:29]
    password = word[29:]
    return salt, password

#cracks a variation of blowfish py-bcrypt
#use at own risk close to one second per hash
def nixBlowfish(hashx, dictionary, shared):
    salt, password = nixBlowfishSort(hashx)
    a = datetime.datetime.now()
    for word in dictionary:
        word = word.rstrip()
        if bcrypt.hashpw(word, salt) == (salt + password):
            time = datetime.datetime.now() - a
            return word
