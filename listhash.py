import crypt
import hashlib
import bcrypt


def nixSha512list(dictionary, outputFile, listSalt):
    for word in dictionary:
        word = word.rstrip()
        hashed = crypt.crypt(word, listSalt)
        outputFile.write(word + '|' + hashed +'\n')

""" Produces a list of hashes from
your input dictionary file. This
supports the crypt library."""
def makeHashList(listName, listType, dictionary, listSalt):
    listName = 'lists/' + listName
    outputFile = open(listName, 'w+')
    if listType == 'nixSha512':
        nixSha512list(dictionary, outputFile, listSalt)
    if listType == 'nixBlowfish':
        pass
    if listType == 'sha1':
        pass
    if listType == 'sha224':
        pass
    if listType == 'sha256':
        pass
    if listType == 'sha384':
        pass
    if listType == 'sha512':
        pass
    if listType == 'md5':
        pass
