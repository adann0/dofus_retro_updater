#!/usr/bin/env python3

import os
import sys
import tarfile

import shutil
import cloudscraper

DOFUS_RETRO_URL = "https://download.dofus.com/retro/zip/linux64"
INSTALL_FOLDER = "retro"
ARCHIVE_NAME = "retro.tar.gz"

def download() :
    """
    Télécharge la dernière version de 'retro.tar.gz' depuis le site officiel,
    dans le répertoire courrant.
    
    Retourne True si le téléchargement c'est bien déroulé, False sinon.
    
    Le site est protégé par CloudFlare.
    """
    scraper = cloudscraper.create_scraper()
    response = scraper.get(DOFUS_RETRO_URL, stream=True)
    print("[+] Downloading... (Response from the Server : %s)" % response.status_code)
    if response.status_code == 200 :
        with open(ARCHIVE_NAME, "wb") as f:
            # Progression bar from : https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads
            total_length = response.headers.get('content-length')
            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()
        print("\n[+] OK.")
        return(True)
    else :
        print("[-] Can't download the file.")
        return(False)

def untar() :
    """Untar le fichier 'retro.tar.gz' dans le repertoire 'retro'."""
    print("[+] Extracting...")
    tar = tarfile.open(ARCHIVE_NAME, "r:gz")
    tar.extractall(path=INSTALL_FOLDER)
    tar.close()
    print("[+] OK.")

def rmtar() :
    """Suprimme le fichier 'retro.tar.gz' après l'avoir décompressé."""
    os.remove(ARCHIVE_NAME)

def mkdir() :
    """
    Supprime les anciens répertoires et crée les répertoires necessaires pour l'installation."""
    print("[+] Clean Env...")
    if os.path.exists(INSTALL_FOLDER) :
        print("[+] Dofus Retro already exist. Removing all old files for a fresh install...")
        shutil.rmtree(INSTALL_FOLDER)
    if os.path.exists(ARCHIVE_NAME) :
        os.remove(ARCHIVE_NAME)
    os.mkdir(INSTALL_FOLDER)
    print("[+] OK.")

def main() :
    print("*** DOFUS RETRO UPDATER for Linux [v0.0.1] ***")
    mkdir()
    if download() :
        untar()
        rmtar()

if __name__ == "__main__" :
	main()