# dofus_retro_updater

Un script d'installation et d'update pour le Client Dofus Retro sous Linux.

Pour télécharger l'executable vous pouvez cliquer ici.

## Devs

### Dependencies

	$ sudo apt install git python3-venv python3-pip

### Env

	$ git clone https://github.com/adann0/dofus_retro_updater.git &&
	cd dofus_retro_updater &&
	python3 -m venv venv &&
	source venv/bin/activate &&
	pip install -r requirements.txt

### Build

	make build

L'executable se trouve dans `dist/dofus_retro_updater`