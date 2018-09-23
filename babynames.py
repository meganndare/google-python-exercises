#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

Here's what the html looks like in the baby.html files:
I will extract the year and rank information from these lines.
...
<input type="text" name="year" id="yob" size="4" value="1990">
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, "rU")
  fileContents = f.read()

  year = re.search(r'<.*name.*year.*value\s*=\s*"(\d\d\d\d)"\s*>', fileContents)
  nameData = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', fileContents)

  # Populate dictionary with rank info for each name, using the highest rank for names that are repeated
  rankings = {}

  for rank in nameData:
    if rankings.get(rank[1]):
      rankings[rank[1]] = min(rankings[rank[1]], rank[0])
    else:
      rankings[rank[1]] = rank[0]

    if rankings.get(rank[2]):
      rankings[rank[2]] = min(rankings[rank[2]], rank[0])
    else:
      rankings[rank[2]] = rank[0]

  # Convert the dictionary to a list to return, beginning the list with the year
  babyNames = [year.group(1)]

  for key in sorted(rankings.keys()):
    babyNames.append(key + " " + rankings[key])

  return babyNames


def main():
  args = sys.argv[1:]

  if not args:
    print('usage: file [file ...]')
    sys.exit(1)
  
  # Print ranking data to a separate file for each year data set submitted
  for i in range(len(args)):
    nameData = extract_names(args[i])
    with open("popularNames_"+nameData[0]+".txt", "w") as f:
      for item in nameData:
        f.write("%s\n" % item)

  print("File writing completed. Please check popularNames_{year}.txt")
  
if __name__ == '__main__':
  main()
