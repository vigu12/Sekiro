#!/bin/bash

echo "🔧 Installing Go-based recon tools..."

# Go Tools
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/tomnomnom/assetfinder@latest
go install github.com/owasp-amass/amass/v3/...@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/tomnomnom/gau@latest
go install github.com/hakluke/hakrawler@latest

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
  git clone https://github.com/makefu/dnsmap.git tools/dnsmap
  cd tools/dnsmap && make && cd ../..
fi

# APT dependencies
echo "🧰 Installing APT dependencies..."
sudo apt update
sudo apt install -y dnsenum dnsutils whois curl git make python3-pip

echo "🎯 All tools ready. Happy hunting with Sekiro!"
