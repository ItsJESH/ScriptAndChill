#!/usr/bin/env python3
import sys
import os
import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed

def getDoc(uri,savePath):
    try:
        docName = unquote(uri.split("/")[-1])
        filePath = os.path.join(savePath, docName)
        print("[+] Name:", docName)
        if os.path.exists(filePath):
            print(f"[-] {docName} already exists at {os.path.abspath(savePath)}! Skipping...")
            return
        print("[+] Downloading:", docName)
        res = req.get(uri)
        if res.status_code == 200:
            with open(filePath, "wb") as f:
                f.write(res.content)
            print(f"[+] {docName} saved to {os.path.abspath(savePath)}!")
        else:
            print(f"[-] Failed to download {docName}! Status: {res.status_code}")
    except req.exceptions.RequestException as e:
        print(f"[-] Error downloading {uri}: {e}")

def fetchData(uri):
    try:
        print(f"[+] Sending request to {uri}")
        res = req.get(uri)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href == '../':
                continue
            full_url = urljoin(uri, href)
            if urlparse(full_url).netloc == urlparse(uri).netloc:
                links.append(full_url)
        return links
    except req.exceptions.RequestException as e:
        print(f"[-] Error fetching the page: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("[!] Usage: script.py <URL> <PATH>")
        sys.exit(1)

    uri = sys.argv[1]
    savePath=sys.argv[2]
    print(f"[+] Fetching data from: {uri}")

    resData = fetchData(uri)
    doneData = set()
    download_tasks = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        while resData:
            turi = resData.pop(0)
            if turi in doneData:
                continue
            doneData.add(turi)

            if turi.endswith(".pdf"):
                print("[+] PDF Found:", turi)
                future = executor.submit(getDoc, turi,savePath)
                download_tasks.append(future)
            elif not turi[-4:].lower().endswith(".pdf") and "." not in turi.split("/")[-1]:
                new_links = fetchData(turi)
                resData.extend(new_links)

        
        for future in as_completed(download_tasks):
            pass 

    print("[+] All tasks complete.")

