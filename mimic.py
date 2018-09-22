#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.


"""

import random
import sys

# Cleans and formats the words from the text file
def clean_file(fileObj):
  data = open(fileObj, 'rU')
  text = str(data.read())

  return text.strip().lower().split()


# Returns mimic dict mapping each word to list of words which follow it.
def mimic_dict(filename):
  words = clean_file(filename)

  mimic_dict = {}
  mimic_dict[""] = [words[0]]
  
  for i in range(len(words) - 1):
    if mimic_dict.get(words[i]):
      current = mimic_dict.get(words[i])
      current.append(words[i+1])
      mimic_dict[words[i]] = current
    else:
      mimic_dict[words[i]] = [words[i+1]]

  return mimic_dict

# Given mimic dict and start word, prints 200 random words.
def print_mimic(mimic_dict, word):
  if word not in mimic_dict:
    print("Word not found in the text file")
    sys.exit(1)

  result = ""

  for i in range(200):
    if word in mimic_dict:
      nexts = mimic_dict.get(word)
      word = random.choice(nexts)
      result = result + word + " "
    else:
      nexts = mimic_dict.get('')
      word = random.choice(nexts)
      result = result + word + " "

  print(result)



# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')

	
if __name__ == '__main__':
  main()
