# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi
import time

# need change list...
keyList = ["\b"]
for char in "IJKLASDY":
  keyList.append(char)

def key_check():
  keys = []
  for key in keyList:
    if wapi.GetAsyncKeyState(ord(key)):
      keys.append(key)
  return keys

if __name__ == '__main__':
  while True:
    print(key_check())