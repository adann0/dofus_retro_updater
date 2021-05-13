#!/usr/bin/env python3

import os
import sys

from dofus_retro_updater.utils import get_desktop_path
from dofus_retro_updater.dlcfbp import download
from dofus_retro_updater.commands import mkdir, rm, untar, mv, chmod

HOME_PATH = os.path.expanduser('~')
GAME_PATH = "/usr/games/retro"
CONF_PATH = os.path.join(HOME_PATH, ".config/Dofus Retro")
DESK_PATH = get_desktop_path()

# Update

def update() :
	# Download
	rm("/tmp/retro.tar.gz")
	print("[+] Updating...")
	if not download("/tmp/retro.tar.gz", "https://download.dofus.com/retro/zip/linux64", bar=True) :
		print("[-] Can't Update... Cancel.")
		return(False)
	# Update
	rm(GAME_PATH)
	mkdir(GAME_PATH)
	untar("/tmp/retro.tar.gz", GAME_PATH)
	rm("/tmp/retro.tar.gz")
	# Shortcut
	add_desktop_shortcut()
	print("\n[+] OK.")

def add_desktop_shortcut() :
	# Icone
	download("/tmp/Dofus Retro.icns", "https://github.com/adann0/dofus_retro_updater/raw/main/Dofus%20Retro.icns")
	mv("/tmp/Dofus Retro.icns", "/usr/games/retro/")
	# Shortcut
	if not DESK_PATH :
		print("[-] You Desktop can't be founded. No Shortcut Icon will be added. You can launch the game by running `$ ./usr/games/retro/dofus1electron`")
	else :
		download("/tmp/Dofus Retro.desktop", "https://github.com/adann0/dofus_retro_updater/raw/main/Dofus%20Retro.desktop")
		mv("/tmp/Dofus Retro.desktop", DESK_PATH)
		chmod(os.path.join(DESK_PATH, "Dofus Retro.desktop"))

# Uninstall

def uninstall() :
	print("[+] Removing all files...")
	rm(GAME_PATH)
	rm(CONF_PATH)
	if DESK_PATH != None :
		rm(os.path.join(DESK_PATH, "Dofus Retro.desktop"))
	else :
		print("[-] Your Desktop can't be founded. No Shortcut Icon will be removed.")
	print("[+] OK.")