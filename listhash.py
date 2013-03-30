import crypt
import hashlib
import bcrypt


def nixSha512list(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = crypt.crypt(word, listSalt)
        outputFile.write(word + '|' + hashed + '\n')


def nixBlowfishlist(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = bcrypt.hashpw(word, listSalt)
        outputFile.write(word + '|' + hashed + '\n')

        
def sha1list(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha1(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')


def sha224list(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha224(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')


def sha256list(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha256(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')


def sha384list(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha384(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')


def sha512list(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.sha512(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')


def md5list(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = hashlib.md5(listSalt + word).hexdigest()
        outputFile.write(word + '|' + hashed + '\n')


""" Produces a list of hashes from your input dictionary file. This
supports the crypt, hashlib, and bcrypt library currently."""
def makeHashList(listName, listType, dictionary, listSalt):
    listName = 'lists/' + listName
    outputFile = open(listName, 'w+')
    if listType == 'nixSha512':
        nixSha512list(dictionary, outputFile, listSalt)
    if listType == 'nixBlowfish':
        nixBlowfishlist(dictionary, outputFile, listSalt)
    if listType == 'sha1':
        sha1list(dictionary, outputFile, listSalt)
    if listType == 'sha224':
        sha224list(dictionary, outputFile, listSalt)
    if listType == 'sha256':
        sha256list(dictionary, outputFile, listSalt)
    if listType == 'sha384':
        sha384list(dictionary, outputfile, listSalt)
    if listType == 'sha512':
        sha512list(dictionary, outputfile, listSalt)
    if listType == 'md5':
        md5list(dictionary, outputfile, listSalt)
