#!/usr/bin/python
import random
import sys

class bcolors:
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  END = '\033[0m'

tab1=[]
tab2=[]
tab3=[]

words = []
file = open('test_file.txt').read().split()
colors = ["red", "red", "red", "blue", "blue", "blue", "grey", "grey", "black"]
role=sys.argv[1]
grille=9

for word in file:
  words.append(word)

def generateWords(role):
  game_words=[]
  i=0
  while i < grille:
    word = words[i]

    if role == "master":
      wordColor=assignColors(word)
      game_words.insert(i, wordColor)

    if role == "player":
      game_words.insert(i, word)

    i=i+1

  return game_words

def assignColors(word):
  color_words=[]
  i=0
  while i < grille:
    color = random.choice(colors)
    colors.remove(color)
    if color == "red":
        return word + '_r'

    if color == "blue":
        return word + '_b'

    if color == "grey":
        return word + '_g'

    if color == "black":
        return word + '_y'

    return 'error'

game=generateWords(role)

tab1=[game[0],game[1],game[2]]
tab2=[game[3],game[4],game[5]]
tab3=[game[6],game[7],game[8]]

for row in zip(tab1, tab2, tab3):
  print ' '.join(row)

j=0
while j < grille:
  print (game[j])
  j=j+1

