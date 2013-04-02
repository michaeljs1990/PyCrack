""" Checks the users hash against a pre computed hash list"""


def splitword(hashx):
    word = hashx.split('|')
    text = word[0]
    hashedtext = word[1]
    hashedtext = hashedtext.rstrip()
    hashedtext = hashedtext.lstrip()
    return text, hashedtext


def crack(word, hashlist, sharedCount, sharedPass):
    for hashx in hashlist:
        text, hashedtext = splitword(hashx)
        sharedCount.value = sharedCount.value + 1
        if word == hashedtext:
            text = text.rstrip()
            sharedPass.value = text
            break
