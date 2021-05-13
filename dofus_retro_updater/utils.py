#!/usr/bin/env python3

import os

HOME_PATH = os.path.expanduser("~")

def get_desktop_path() :
	possibles_desktop_paths = [
		os.path.join(HOME_PATH, "Desktop"),
		os.path.join(HOME_PATH, "Bureau"),
	]
	for possible_desktop_path in possibles_desktop_paths :
		if os.path.exists(possible_desktop_path) :
			return(possible_desktop_path)
