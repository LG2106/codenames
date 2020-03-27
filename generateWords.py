#!/usr/bin/python
import random
import sys

words = ["mot1", "mot2", "mot3", "mot4", "mot5", "mot6", "mot7", "mot8", "mot9", "mot10", "mot11", "mot12"]
colors = ["red", "red", "red", "blue", "blue", "blue", "grey", "grey", "black"]

param=sys.argv[1]
grille=9

def assignColors(word):
  color_words=[]
  i=0
  while i < grille:
    color = random.choice(colors)
    colors.remove(color)
    if color == "red":
        return '\e[0;31m' + word + '\e[0m'

    if color == "blue":
        return '\e[1;34m' + word + '\e[0m'

    if color == "grey":
        return '\e[0;37m' + word + '\e[0m'

    if color == "black":
        return '\e[1;33m' + word + '\e[0m'

    return 'error'

def generateWords(role):
  game_words=[]
  i=0
  while i < grille:
    word = random.choice(words)
    words.remove(word)

    if role == "master":
      wordColor=assignColors(word)
      game_words.insert(i, wordColor)

    if role == "player":
      game_words.insert(i, word)

    i=i+1

  return game_words

game=generateWords(param)

j=0
while j < grille:
  print (game[j])
  j=j+1

