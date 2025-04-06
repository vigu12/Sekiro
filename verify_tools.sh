#!/bin/bash

echo "🔍 Verifying installed tools for Sekiro..."

# Define Go tools
declare -A GO_TOOLS=(
  ["subfinder"]="subfinder"
  ["assetfinder"]="assetfinder"
  ["amass"]="amass"
  ["katana"]="katana"
  ["hakrawler"]="hakrawler"
  ["gau"]="gau"
)

# Define cloned tools
declare -A CLONED_TOOLS=(
  ["fierce"]="tools/fierce/fierce.py"
  ["dnsmap"]="tools/dnsmap/dnsmap"
  ["dnsrecon"]="tools/dnsrecon/dnsrecon.py"
)

# Define system tools
SYSTEM_TOOLS=("dnsenum" "dig" "whois" "curl" "git" "make" "pip3")

echo ""
echo "🚀 [1/3] Checking Go-based tools..."
for tool in "${!GO_TOOLS[@]}"; do
  if command -v "${GO_TOOLS[$tool]}" >/dev/null 2>&1 || [ -f "$HOME/go/bin/${GO_TOOLS[$tool]}" ]; then
    echo "✅ $tool is installed"
  else
    echo "❌ $tool is missing — check Go install or \$PATH"
  fi
done

echo ""
echo "📁 [2/3] Checking Cloned Tools..."
for tool in "${!CLONED_TOOLS[@]}"; do
  if [ -f "${CLONED_TOOLS[$tool]}" ]; then
    echo "✅ $tool is present"
  else
    echo "❌ $tool not found in tools directory"
  fi
done

echo ""
echo "🧰 [3/3] Checking System Tools..."
for bin in "${SYSTEM_TOOLS[@]}"; do
  if command -v "$bin" >/dev/null 2>&1; then
    echo "✅ $bin is installed"
  else
    echo "❌ $bin is missing — run: sudo apt install $bin"
  fi
done

echo ""
echo "✅ Sekiro verification complete. Fix ❌ items before recon!"
