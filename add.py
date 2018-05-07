#!/usr/bin/env python3

from subprocess import Popen
import sys

Popen("echo " + sys.argv[1] + " >> domains.cfg", shell=True)


#if you want to add domain names to domains.cfg you can use "cat" command
#this script is  little bit easier for by one by adding
#example   "add.py example.com"
#example   "cat example.com >> domains.cfg"
