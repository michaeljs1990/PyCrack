#crypto libs
import hashlib
import crypt
import bcrypt
import time

#sorts the nixPwd hash
def nixSha512Sort(word):
    word = word.split('$')
    salt = '$' + word[1] + '$' + word[2] + '$'
    password = word[3].split(':')[0]
    return salt, password

#cracks the sha512 unix hash
def nixSha512(hashx, dictionary, sharedCount, sharedPass):
    salt, password = nixSha512Sort(hashx)
    for word in dictionary:
        word = word.rstrip()
        sharedCount.value = sharedCount.value + 1
        if crypt.crypt(word, salt) == (salt + password):
            sharedPass.value = word
            time.sleep(4)
            break

#sorts blowfish hashs for use in nixBlowfish
def nixBlowfishSort(word):
    salt = word[:29]
    password = word[29:]
    return salt, password

#cracks a variation of blowfish py-bcrypt
#use at own risk close to one second per hash
def nixBlowfish(hashx, dictionary, sharedCount, sharedPass):
    salt, password = nixBlowfishSort(hashx)
    for word in dictionary:
        word = word.rstrip()
        sharedCount.value = sharedCount.value + 1
        if bcrypt.hashpw(word, salt) == (salt + password):
            sharedPass.value = word
            time.sleep(4)
            break
