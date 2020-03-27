#!/usr/bin/python
import random
import sys

fw = open("words.txt", "w")
fw.write('')
fw.close()

fc = open("colors.txt", "w")
fc.write('')
fc.close()

grille = 25
words = []
fileWords = open('dico.txt').read().split()
colors = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'black']

for word in fileWords:
  words.append(word)

def createGameFiles():
  i=0
  while i < grille:
    word = random.choice(words)
    words.remove(word)
    color = random.choice(colors)
    colors.remove(color)

    fw = open("words.txt", "a")
    fw.write(word + ' ')
    fw.close()
    
    fc = open("colors.txt", "a")
    fc.write(color + ' ')
    fc.close()

    i = i+1

game=createGameFiles()

