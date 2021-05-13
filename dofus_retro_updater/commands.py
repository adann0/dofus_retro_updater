#!/usr/bin/env python3

import os

def ask_password_early() :
	os.system("sudo echo '*** DOFUS RETRO UPDATER for Linux ***'")

def mkdir(path) :
	os.system("sudo mkdir '%s'" % path)

def rm(path):
	os.system("sudo rm -rf '%s'" % path)

def untar(archive, destination) :
	os.system("sudo tar -xf '%s' -C '%s'" % (archive, destination))

def mv(file, path) :
	os.system("sudo mv '%s' '%s'" % (file, path))

def chmod(file) :
	os.system("sudo chmod 750 '%s'" % file)
