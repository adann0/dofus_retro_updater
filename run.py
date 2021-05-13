#!/usr/bin/env python3

import sys

from dofus_retro_updater.main import update, uninstall
from dofus_retro_updater.commands import ask_password_early

if __name__ == "__main__" :
	if len(sys.argv) < 2 or not sys.argv[1] in ["update", "uninstall"] :
		sys.exit("USAGE: %s [update|uninstall]" % sys.argv[0])
	ask_password_early()
	if sys.argv[1] == "update" :
		update()
	elif sys.argv[1] == "uninstall" :
		uninstall()
