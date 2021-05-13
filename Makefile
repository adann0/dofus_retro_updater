build:
	pyinstaller run.py --name dofus_retro_updater --onefile --add-data "venv/lib/python3.6/site-packages/cloudscraper:./cloudscraper"

cleanpycache:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

cleanpyinstaller:
	rm -rf dist build dofus_retro_updater.spec

clean:	cleanpycache cleanpyinstaller
