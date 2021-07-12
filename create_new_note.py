#!/usr/bin/env python3

import sys
import datetime
import os

"""This script create a markdown file as a template for the daily notes of this project.
It shall take the month-year fiolder and create a note with the date in there.
"""

def main():
  today = datetime.date.today()
  current_date = str(today)
  foldername = f"{today.year}_{today.month:02d}"
  extension = ".md"
  filename = F"{current_date}_learning_journal{extension}"
  print(filename)
  print(foldername)
  if not os.path.exists(os.path.join(os.getcwd(), foldername)):
    os.makedirs(os.path.join(os.getcwd(), foldername))
    print(f"Directory {os.path.join(os.getcwd(), foldername)} created")
  path_file = os.path.join(os.getcwd(), foldername, filename)
  if(os.path.isfile(path_file)):
    print(f"{path_file} exists")
  else:
    print(f"{path_file} does not exists")
    with open(path_file, "w") as f:
      f.write(f"# Daily Learning Journal - {current_date} - {today.strftime('%A')}")



  pass
 
if __name__ == "__main__":
  main()
