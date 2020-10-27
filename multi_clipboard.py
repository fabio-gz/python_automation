#!/usr/bin/python3
"""
Updatable multi-clipboard
"""
import shelve
import pyperclip
import sys

shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    shelf[sys.argv[2]] == pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(shelf.keys())))
    elif sys.argv[1] in shelf:
        pyperclip.copy(shelf[sys.argv[1]])

shelf.close()
