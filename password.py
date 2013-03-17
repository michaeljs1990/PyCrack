#Looks in password.txt for passwords and evaluates the function
#that should be called to crack it.
import crack


dictionary = open('config/dict.txt', 'r+')
file = open('config/cracklist.txt', 'r+')

for word in file:
    word = word.rstrip('\n')
    print word
   # if '$6$' in word:
   #     crack.nixSha512(word, dictionary)
    if '$2a$12$' in word:
        crack.nixBlowfish(word, dictionary)
