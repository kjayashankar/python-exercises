# python-3
import random

v = 'aeiou'
c = 'bcdfghjklmnpqrstvwxyz'
al = v+c

def setpreference():
    print('enter v for vowels, c for consonents and i for any letter')
    letter1 = input('enter 1st group of your choice\n')
    while(letter1 not in 'vci'):
        print('wrong option')
        print('enter v for vowels, c for consonents and i for any letter')
        letter1 = input('enter 1st group of your choice\n')
    letter2 = input('enter 2nd group of your choice\n')
    while(letter2 not in 'vci'):
        print('wrong option')
        print('enter v for vowels, c for consonents and i for any letter')
        letter2 = input('enter 2nd group of your choice\n')
    letter3 = input('enter 3rd group of your choice\n')
    while(letter3 not in 'vci'):
        print('wrong option')
        print('enter v for vowels, c for consonents and i for any letter')
        letter3 = input('enter 3rd group of your choice\n')
    prefs = [letter1,letter2,letter3]
    maxima = input('enter the max number of options you want to see\n')
    while(not maxima.isdigit() or int(maxima) <= 0):
        print('invalid integer')
        maxima = (input('enter the max number of options you want to see\n'))
    return prefs,int(maxima)

def generate(pref):
    if pref == 'v':
        return random.choice(v)
    elif pref == 'c':
        return random.choice(c)
    else:
        return random.choice(al)

if __name__ == '__main__':
    print('hey there')
    prefs,maxima = setpreference()
    for index in range(maxima):
        output = ''
        output = ''.join(generate(x) for x in prefs)
        print(output)
