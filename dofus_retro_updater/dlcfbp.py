#!/usr/bin/env python3

"""
dlcfbp.py (DownLoad CloudFlare ByPass)

Download a file on a website protected by CloudFlare.

USAGE: ./dlcfbp [filename] [url]
"""

import sys
import re
import cloudscraper
import requests

def download(filename, url, bar=False) :
    scraper = cloudscraper.create_scraper()
    try :
    	response = scraper.get(url, stream=True)
    except requests.exceptions.ConnectionError:
    	return(False) # wifi down
    if response.status_code == 200 :
        with open(filename, "wb") as f:
            # Progression bar from : https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads
            total_length = response.headers.get('content-length')
            if total_length is None or not bar : # no content length header
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
        return(True)
    else :
        return(False) # can't download the file

if __name__ == "__main__" :
    if len(sys.argv) < 3 or not sys.argv[2].startswith("http") :
        sys.exit("USAGE: ./dlcfbp [filename] [url]")
    if download(sys.argv[1], sys.argv[2]) :
        sys.exit(0)
    else :
        sys.exit(1)