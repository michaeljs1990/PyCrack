import crypt
import hashlib
import bcrypt


""" This is used to make a prehashed list from the input dictionary
select by the user. The user sets the salt to use from the interface.
Read the wiki for more infromation on proper use of salts."""


def nixSha512list(dictionary, outputFile, listSalt, sharedCount):
    for word in dictionary:
        word = word.rstrip()
        hashed = crypt.crypt(word, listSalt)
        outputFile.write(word + '|' + hashed + '\n')
        sharedCount.value = sharedCount.value + 1


def nixBlowfishlist(dictionary, outputFile, listSalt, sharedCount):
    for word in dictionary:
        word = word.rstrip()
        hashed = bcrypt.hashpw(word, listSalt)
        outputFile.write(word + '|' + hashed + '\n')
        sharedCount.value = sharedCount.value + 1

        
def sha1list(dictionary, outputFile, listSalt, sharedCount):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha1(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')
        sharedCount.value = sharedCount.value + 1


def sha224list(dictionary, outputFile, listSalt, sharedCount):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha224(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')
        sharedCount.value = sharedCount.value + 1


def sha256list(dictionary, outputFile, listSalt, sharedCount):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha256(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')
        sharedCount.value = sharedCount.value + 1


def sha384list(dictionary, outputFile, listSalt, sharedCount):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha384(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')
        sharedCount.value = sharedCount.value + 1


def sha512list(dictionary, outputFile, listSalt, sharedCount):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha512(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')
        sharedCount.value = sharedCount.value + 1


def md5list(dictionary, outputFile, listSalt, sharedCount):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.md5(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')
        sharedCount.value = sharedCount.value + 1


""" Produces a list of hashes from your input dictionary file. This
supports the crypt, hashlib, and bcrypt library currently."""
def makeHashList(listName, listType, dictionary, listSalt, sharedCount):
    listName = 'lists/' + listName
    outputFile = open(listName, 'w+')
    if listType == 'nixSha512':
        nixSha512list(dictionary, outputFile, listSalt, sharedCount)
    if listType == 'nixBlowfish':
        nixBlowfishlist(dictionary, outputFile, listSalt, sharedCount)
    if listType == 'sha1':
        sha1list(dictionary, outputFile, listSalt, sharedCount)
    if listType == 'sha224':
        sha224list(dictionary, outputFile, listSalt, sharedCount)
    if listType == 'sha256':
        sha256list(dictionary, outputFile, listSalt, sharedCount)
    if listType == 'sha384':
        sha384list(dictionary, outputfile, listSalt, sharedCount)
    if listType == 'sha512':
        sha512list(dictionary, outputfile, listSalt, sharedCount)
    if listType == 'md5':
        md5list(dictionary, outputfile, listSalt, sharedCount)
