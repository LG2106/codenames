#!/usr/bin/python
import random
import sys
import TableIt

R = "\033[0;31;40m"
B = "\033[0;36;40m"
G = "\033[0;37;40m"
Y = "\033[0;33;40m"
E = "\033[0m"

words = []
fileWords = open('words.txt').read().split()
colors = []
fileColors = open('colors.txt').read().split()

role=sys.argv[1]
grille=25

for word in fileWords:
  words.append(word)

for color in fileColors:
  colors.append(color)

def generateWords(role):
  game_words=[]
  i=0
  while i < grille:
    word = words[i]

    if role == "master":
      wordColor=assignColors(word,i)
      game_words.insert(i, wordColor)

    if role == "player":
      game_words.insert(i, word)

    i=i+1

  return game_words

def assignColors(word,i):
  color = colors[i]
  
  if color == "red":
    return R + word + E
  
  if color == "blue":
    return B + word + E

  if color == "grey":
    return G + word + E

  if color == "black":
    return Y + word + E

  return 'error'

game=generateWords(role)

n=5
newList=[game[n*i : n*(i+1)] for i in range(n)]

TableIt.printTable(newList)

j=0
while j < grille:
#  print (game[j])
  j=j+1

