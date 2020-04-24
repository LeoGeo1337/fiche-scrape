#-*- coding: utf-8 -*-
#
#creates a list of all possible combinations alphalower_numeric 4 char
#you can always change it with like [alphanum = range(a-z)] or someshit, but i didnt want to do that.
#
#this script creates a list for termscrape
#
#made by <L 3 0 N 1 D U S>
#
#
#
# ooooo   ooooo ooooooooooooo ooooooooo.
# `888'   `888' 8'   888   `8 `888   `Y88.
#  888     888       888       888   .d88'
#  888ooooo888       888       888ooo88P'
#  888     888       888       888
#  888     888       888       888
# o888o   o888o     o888o     o888o
#
#
#
import itertools
def htp():
    alphanum = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
    #test = ["a","b","c","1","2","3"]
    string = list(itertools.permutations(alphanum, 4))
    file = open("list.txt", "w")
    for x in string:
        #print(''.join(x))
        file.write(str(''.join(x))+'\n')
    file.close()
htp()
