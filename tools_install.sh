#!/bin/bash

echo "🔧 Installing Go-based recon tools..."

# Go Tools
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/tomnomnom/assetfinder@latest
go install github.com/owasp-amass/amass/v3/...@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/tomnomnom/gau@latest
go install github.com/hakluke/hakrawler@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install github.com/ferreiraklet/shosubgo@latest
go install github.com/abhaybhargav/github-subdomains@latest

echo "✅ Go tools installed successfully."

echo "📁 Setting up recon tools..."

# Create tools directory
mkdir -p tools

# DNSRecon with virtualenv
if [ ! -d "tools/dnsrecon" ]; then
  git clone https://github.com/darkoperator/dnsrecon.git tools/dnsrecon
  python3 -m venv tools/dnsrecon/venv
  source tools/dnsrecon/venv/bin/activate
  pip install -r tools/dnsrecon/requirements.txt
  deactivate
fi

# Fierce
if [ ! -d "tools/fierce" ]; then
  git clone https://github.com/mschwager/fierce.git tools/fierce
fi

# DNSmap
if [ ! -d "tools/dnsmap" ]; then
  git clone https://github.com/resurrecting-open-source-projects/dnsmap.git tools/dnsmap
  cd tools/dnsmap && make && cd ../..
fi

# ParamSpider
if [ ! -d "tools/paramspider" ]; then
  git clone https://github.com/devanshbatham/ParamSpider.git tools/paramspider
fi

# Arjun
if [ ! -d "tools/arjun" ]; then
  git clone https://github.com/s0md3v/Arjun.git tools/arjun
fi

# xnLinkFinder
if [ ! -d "tools/xnLinkFinder" ]; then
  git clone https://github.com/xnl-h4ck3r/xnLinkFinder.git tools/xnLinkFinder
fi

# DNSDumpster script
if [ ! -d "tools/dnsdumpster" ]; then
  git clone https://github.com/PaulSec/API-dnsdumpster.com.git tools/dnsdumpster
fi

# Knockpy
if [ ! -d "tools/knockpy" ]; then
  git clone https://github.com/guelfoweb/knock.git tools/knockpy
fi

# VirusTotal Search Tool
if [ ! -d "tools/virustotal" ]; then
  git clone https://github.com/eduardxyz/virustotal-search.git tools/virustotal
fi

# Censys Search Tool
if [ ! -d "tools/censys" ]; then
  git clone https://github.com/christophetd/censys-subdomain-finder.git tools/censys
fi

# Wordlists setup (optional but recommended)
if [ ! -d "wordlists" ]; then
  mkdir wordlists
  echo "⚡ Downloading SecLists..."
  git clone https://github.com/danielmiessler/SecLists.git wordlists/SecLists
fi

# APT dependencies
echo "🧰 Installing APT dependencies..."
sudo apt update
sudo apt install -y dnsenum dnsutils whois curl git make python3-pip python3-venv jq massdns

# Python dependencies
echo "🐍 Installing Python modules from requirements.txt..."
pip3 install -r requirements.txt

echo "🎯 All tools and dependencies installed successfully! Happy hunting with Sekiro!"
