# tag.py
Simple Tag function in python to add Tags and Values to Operating Systems for automation purposes

Tag was written to allow tags and values to be added to individual hosts to aid automation scripting and tools such as Ansible. While Tags have been around in software such as VMware, and Cloud providers, I couldn't find anything that was written specifically for the task at thee host OS level.

### Usage

tag.py add|delete|get|view|reset|help tag value 

### Examples

tag.py add OS Linux dplevel 4 - This will add 2 tags OS:Linux & dplevel:4

tag.py delete OS - This will delete the OS tag and its value

tag.py get dplevel - This will return the value for tag dplevel

tag.py reset - This will wipe the tags database

### Future 

* Replace option
* Ansible Module
* Ask where to store the DB
* Allow deletion of more than 1 tag at a time

### Credit

Thanks to [Palash Bauri](https://www.freecodecamp.org/news/author/palash/), who's [code](https://www.freecodecamp.org/news/how-to-write-a-simple-toy-database-in-python-within-minutes-51ff49f47f1/) was the starting point for this project until I butchered it 
