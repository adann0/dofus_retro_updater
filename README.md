# dofus_retro_updater

Un script d'installation et d'update pour Dofus Retro sous Linux.

# Dependencies

	$ sudo apt install git python3-venv

# Env

	$ git clone https://github.com/adann0/dofus_retro_updater.git &&
	cd dofus_retro_updater &&
	python3 -m venv venv &&
	source venv/bin/activate &&
	pip install -r requirements.txt

# Run

	./dofus_retro_updater update # install ou update le jeu
	./dofus_retro_updater uninstall # uninstall le jeu
