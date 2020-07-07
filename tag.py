#!/usr/bin/python3

#tag.py written by Phil Dunn 07/07/2020
#Version 0.1

import json
import os
import sys

class tagDB(object):
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self , location):
       if os.path.exists(location):
           self._load()
       else:
            self.db = {}
       return True

    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

    def set(self , tag, value):
        try:
            self.db[str(tag)] = value 
            self.dumpdb()
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self , tag):
        try:
            return self.db[tag]
        except KeyError:
            print("No Value Can Be Found for " + str(tag))
            return False

    def view(self):
        try:
            return self.db
        except KeyError:
            print("No tags can be found")
            return False

    def delete(self , tag):
        if not tag in self.db:
            return False
        del self.db[tag]
        self.dumpdb()
        return True
    
    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True


mydb = tagDB("./tagdb.db")
_newargs = int((int(len(sys.argv))- 2)/2) 
_argcount = int(2)
_keycount = int(3)

if sys.argv[1] == "add":
  print ("adding " + str(_newargs) + " tags")
  for x in range(_newargs):
    mydb.set(sys.argv[_argcount], sys.argv[_keycount]) #Sets Value
    print("Adding Tag: " + sys.argv[_argcount] + ": " + sys.argv[_keycount])
    _keycount += 2
    _argcount += 2

if sys.argv[1] == "delete":
  mydb.delete(sys.argv[2])
  print("Deleting Tag: " + sys.argv[2])

if sys.argv[1] == "get":
  _display = mydb.get(sys.argv[_argcount])
  print (_display)

if sys.argv[1] == "view":
  _display = mydb.view()
  print (_display)

if sys.argv[1] == "reset":
  mydb.resetdb()

if sys.argv[1] == "help":
  print("Usage: tag.py add|delete|get|view|reset|help tag value - Note: multiple tags can be used with the add operator")
  print("Example: tag.py add OS Linux dplevel 4 - This will add 2 tags OS:Linux & dplevel:4")
  print("Example: tag.py delete OS - This will delete the OS tag and its value")
  print("Example: tag.py get dplevel - This will return the value for tag dplevel")
  print("Example: tag.py reset - This will wipe the tags database")
