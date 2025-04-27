#!/bin/bash

echo "🔍 Verifying installed tools for Sekiro Ultimate..."

# === Define Go tools ===
declare -A GO_TOOLS=(
  ["subfinder"]="subfinder"
  ["assetfinder"]="assetfinder"
  ["amass"]="amass"
  ["katana"]="katana"
  ["hakrawler"]="hakrawler"
  ["gau"]="gau"
  ["httpx"]="httpx"
  ["nuclei"]="nuclei"
  ["naabu"]="naabu"
  ["shosubgo"]="shosubgo"
  ["github-subdomains"]="github-subdomains"
)

# === Define cloned (Python) tools ===
declare -A CLONED_TOOLS=(
  ["fierce"]="tools/fierce/fierce.py"
  ["dnsmap"]="tools/dnsmap/dnsmap"
  ["dnsrecon"]="tools/dnsrecon/dnsrecon.py"
  ["paramspider"]="tools/paramspider/paramspider.py"
  ["arjun"]="tools/arjun/arjun.py"
  ["xnLinkFinder"]="tools/xnLinkFinder/xnLinkFinder.py"
  ["dnsdumpster"]="tools/dnsdumpster/dnsdumpster.py"
  ["knockpy"]="tools/knockpy/knockpy.py"
  ["virustotal"]="tools/virustotal/virustotal.py"
  ["censys"]="tools/censys/censys.py"
)

# === Define system-installed tools ===
SYSTEM_TOOLS=("dnsenum" "dig" "whois" "curl" "git" "make" "pip3" "massdns")

# === Checking Go-based tools ===
echo ""
echo "🚀 [1/4] Checking Go-based tools..."
for tool in "${!GO_TOOLS[@]}"; do
  if command -v "${GO_TOOLS[$tool]}" >/dev/null 2>&1 || [ -f "$HOME/go/bin/${GO_TOOLS[$tool]}" ]; then
    echo "✅ $tool is installed"
  else
    echo "❌ $tool is missing — check Go install or \$PATH"
  fi
done

# === Checking Cloned tools ===
echo ""
echo "📁 [2/4] Checking Cloned Python Tools..."
for tool in "${!CLONED_TOOLS[@]}"; do
  if [ -f "${CLONED_TOOLS[$tool]}" ]; then
    echo "✅ $tool is present"
  else
    echo "❌ $tool not found in tools directory"
  fi
done

# === Checking System Tools ===
echo ""
echo "🧰 [3/4] Checking System Tools..."
for bin in "${SYSTEM_TOOLS[@]}"; do
  if command -v "$bin" >/dev/null 2>&1; then
    echo "✅ $bin is installed"
  else
    echo "❌ $bin is missing — run: sudo apt install $bin"
  fi
done

# === Checking Python Requirements Installed ===
echo ""
echo "🐍 [4/4] Checking Python Modules from requirements.txt..."
MISSING_MODULES=0
REQUIRED_MODULES=("sublist3r" "dnspython" "requests" "shodan" "censys" "python-whois" "python-dotenv" "urllib3" "beautifulsoup4")

for module in "${REQUIRED_MODULES[@]}"; do
  python3 -c "import $module" >/dev/null 2>&1
  if [ $? -eq 0 ]; then
    echo "✅ Python module '$module' installed"
  else
    echo "❌ Missing Python module '$module' — run: pip3 install $module"
    MISSING_MODULES=$((MISSING_MODULES+1))
  fi
done

# === Final Summary ===
echo ""
if [ $MISSING_MODULES -eq 0 ]; then
  echo "✅ Sekiro verification complete! All systems go! 🚀"
else
  echo "⚠️ $MISSING_MODULES Python modules missing. Fix before using Sekiro!"
fi
