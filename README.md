# 🐺 Sekiro - Recon Framework

███████╗███████╗██╗  ██╗██╗██╗██████╗  ██████╗ 
██╔════╝██╔════╝╚██╗██╔╝██║██║██╔══██╗██╔═══██╗
███████╗█████╗   ███╔╝  ██║██║██████╔╝██║   ██║
╚════██║██╔══╝   ██╔██╗ ██║██║██╔═══╝ ██║   ██║
███████║███████╗██╔╝ ██╗██║██║██║     ╚██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝      ╚═════╝ 



**Sekiro** is a powerful, all-in-one **reconnaissance CLI tool** built for bug bounty hunters, red teamers, and penetration testers.  
Inspired by the *One-Arm Wolf*, it slices through targets using the sharpest tools in the recon arsenal.

> ⚔️ Developed by **Vignesh (chip)**

---

## ✨ Features

- 🔍 **Modular CLI Menu**: Choose Passive, Deep, or DNS Recon
- 🧰 **Multi-tool Integration**: Runs subfinder, amass, assetfinder, katana, and more
- 📁 **Structured Output**: Auto-saves to `output/<target>/toolname_timestamp.txt`
- 💡 **Live Tee Output**: See real-time scan + logs
- ⚡ **Fast & Lightweight**: No bloat, pure speed
- 🧠 **Extensible**: Add tools or modules easily

---

## 🧪 Supported Tools

### 🔎 Passive Recon
- `subfinder`
- `assetfinder`
- `amass (passive)`
- `sublist3r`
- `chaos`
- `github-subdomains`
- `virustotal`
- `censys`

### 🕵 Deep Recon
- `waybackurls`
- `katana`
- `gau`
- `hakrawler`

### 🌐 DNS Recon
- `dnsrecon`
- `dnsenum`
- `dnsmap`
- `dig`
- `fierce`

---



Install Python Dependencies
pip3 install -r requirements.txt


 Install Recon Tools
chmod +x tools_install.sh
./tools_install.sh

Usage

python3 sekiro.py
You’ll be greeted with the Sekiro CLI:

[1] Passive Recon
[2] Deep Recon
[3] DNS Recon
Select option:
Enter your target when prompted, and let the blades fly 🔪

📂 Output Format
All recon results are saved under:

php-template
output/<target>/
├── subfinder_<timestamp>.txt
├── amass_<timestamp>.txt
└── ...

📜 License
This project is licensed under the MIT License.
Feel free to use, share, and improve.

🤝 Contribute
Pull requests welcome!
Create issues for bugs or ideas.
Let’s build a lethal recon beast together 🐉

🔗 Connect
Made with ❤️ by Vignesh (chip)
Tag me if you’re using it or have ideas — let’s link up, hacker fam 🧠⚔️
