
# Script And Chill

> **Automate the boring stuff, script the fun stuff.**  
> Because clicking is for amateurs. 🖱️🚫

---

## 📜 What is this?

Welcome to **Script And Chill** — a collection of scripts that say:  
_"Manual work? Nah bro, we automated that."_ 😎💻

This repo is your friendly toolbox for automation tasks that you *shouldn't* be doing manually in the first place. From scraping files to doing sneaky sysadmin magic, we've got you covered.

---

## 🚀 Current Scripts

| Script               | Description                                                     | Links                                                                                   |
|----------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **DownloadAllPDFs.py** | [📄 Description](#downloadallpdfspy) | [File](https://github.com/ItsJESH/ScriptAndChill/blob/main/DownloadAllPDFs.py) |


---
## 📥 DownloadAllPDFs.py

🔗 [DownloadAllPDFs.py](https://github.com/ItsJESH/ScriptAndChill/blob/main/DownloadAllPDFs.py)

**🧾 Purpose:**  
This script is designed to download **all PDF files** from a target website that allows **Local File Inclusion (LFI)** or open directory listing. Perfect for pentesters, digital hoarders, or the gloriously lazy.

### ⚙️ How it Works

1. 🔍 Scans the target URL for files and subdirectories.
2. 🕵️ Recursively digs into subfolders.
3. 📄 Detects `.pdf` files and queues them for download.
4. 💾 Downloads and saves them to a specified folder.

### 🛠️ Usage

```bash
python3 DownloadAllPDFs.py <URL> <PATH>
````


### 💡 Requirements

* Python 3.x 🐍
* `requests`
* `beautifulsoup4`

📦 Install them via pip:

```bash
pip3 install requests beautifulsoup4
```

---

## ⚠️ Disclaimer

🚨 **Use responsibly.** Those scripta are here to make your life easier, not land you in court. It's meant for ethical use only — like grabbing files from your own servers, testing with permission, or showing off your automation chops. Don’t be that person who uses it to poke around places they shouldn’t — unauthorized access is illegal, uncool, and will get you uninvited from all the good LAN parties. Use it responsibly, script smart, and stay out of trouble. 😎🧑‍💻

We do **NOT** encourage misuse or illegal activities. 🕵️‍♂️🚫

---

## 🤘 Contributing

Got a script that saves time or makes you feel like a lazy genius?
PRs welcome. Let’s automate the world, one task at a time.

---

## 🧊 Stay Chill, Script Smart
