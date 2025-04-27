from datetime import datetime
import os
import subprocess
import time

# === Colors ===
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

# === Banner ===
SEKIRO_BANNER = r"""
_________ ___________  ____  __. .___  __________  ________
 /   _____/ \_   _____/ |    |/ _| |   | \______   \ \_____  \
 \_____  \   |    __)_  |      <   |   |  |       _/  /   |   \
 /        \  |        \ |    |  \  |   |  |    |   \ /    |    \
/_______  / /_______  / |____|__ \ |___|  |____|_  / \_______
        \/          \/          \/               \/          \

          Sekiro Recon Framework (Ultimate)
         Developed by Vignesh (chip) + enhanced
------------------------------------------------
"""

# === Recon Modes ===
RECON_MODES = {
    1: ("Passive Recon", [
        "subfinder", "assetfinder", "amass_passive", "sublist3r",
        "github-subdomains", "shosubgo", "virustotal", "censys"
    ]),
    2: ("Deep Recon", [
        "waybackurls", "katana", "gau", "hakrawler",
        "paramspider", "arjun", "xnLinkFinder"
    ]),
    3: ("DNS Recon", [
        "dnsrecon", "dnsenum", "dnsmap", "dig", "fierce",
        "massdns", "dnsdumpster", "knockpy"
    ]),
    4: ("Advanced Recon", [
        "httpx", "nuclei", "naabu"
    ])
}

# === Tool Command Mappings ===
TOOL_COMMANDS = {
    "subfinder": ["subfinder", "-d", "{}", "-all", "-recursive", "-silent"],
    "assetfinder": ["assetfinder", "--subs-only", "{}"],
    "amass_passive": ["amass", "enum", "-passive", "-d", "{}", "-timeout", "30", "-max-dns-queries", "5000"],
    "sublist3r": ["python3", "/usr/lib/python3/dist-packages/sublist3r.py", "-d", "{}", "-t", "50"],
    "waybackurls": ["bash", "-c", "echo {} | waybackurls"],
    "katana": ["katana", "-u", "{}", "-jc", "-c", "5", "-d", "3"],
    "gau": ["gau", "{}", "--subs", "--threads", "5"],
    "hakrawler": ["hakrawler", "-url", "{}", "-depth", "2", "-plain"],
    "dnsrecon": ["dnsrecon", "-d", "{}", "-a", "-b", "-t", "std"],
    "dnsenum": ["dnsenum", "{}", "-p", "0", "-f", "wordlists/subdomains-top1million-110000.txt"],
    "dnsmap": ["dnsmap", "{}", "wordlists/subdomains-top1million-110000.txt"],
    "dig": ["dig", "any", "{}", "+short"],
    "fierce": ["fierce", "--domain", "{}"],
    "massdns": ["massdns", "-r", "resolvers.txt", "-t", "A", "-o", "S", "-w", "massdns_output.txt", "domains.txt"],
    "github-subdomains": ["github-subdomains", "-d", "{}"],
    "shosubgo": ["shosubgo", "-d", "{}", "-s", "shodan,censys,fofa"],
    "paramspider": ["python3", "tools/paramspider/paramspider.py", "--domain", "{}"],
    "arjun": ["python3", "tools/arjun/arjun.py", "-u", "http://{}", "--get", "--post", "--threads", "10"],
    "xnLinkFinder": ["python3", "tools/xnLinkFinder/xnLinkFinder.py", "-i", "http://{}", "-d", "2"],
    "httpx": ["httpx", "-u", "{}" , "-status-code", "-title", "-tech-detect", "-ip"],
    "nuclei": ["nuclei", "-u", "{}", "-severity", "critical,high,medium"],
    "naabu": ["naabu", "-host", "{}", "-p", "-", "-top-ports", "1000"],
    "dnsdumpster": ["python3", "tools/dnsdumpster/dnsdumpster.py", "-d", "{}"],
    "knockpy": ["python3", "tools/knockpy/knockpy.py", "{}"],
    "virustotal": ["python3", "tools/virustotal/virustotal.py", "-d", "{}", "-o", "output.txt"],
    "censys": ["python3", "tools/censys/censys.py", "-d", "{}", "-export"]
}

# === Clear Screen ===
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# === Menu ===
def print_menu():
    clear()
    print(SEKIRO_BANNER)
    print("Choose your recon mode:\n")
    for idx, (mode, _) in RECON_MODES.items():
        print(f"  [{idx}] {mode}")
    print("  [0] Exit\n")

# === Run Tool ===
def simulate_tool_run(tool, target):
    print(f"\n{Color.CYAN}▶ Running {tool} on {target}...{Color.RESET}")

    clean_target = target.replace("https://", "").replace("http://", "").strip("/")
    output_dir = f"output/{clean_target}/{tool}"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{output_dir}/output_{timestamp}.txt"

    cmd = TOOL_COMMANDS.get(tool)
    if not cmd:
        print(f"{Color.RED}❌ Tool '{tool}' not configured.{Color.RESET}")
        return

    formatted_cmd = [arg.format(target) if '{}' in arg else arg for arg in cmd]

    try:
        with open(file_path, "a") as f:
            process = subprocess.Popen(formatted_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(f"{Color.YELLOW}{line.strip()}{Color.RESET}")
                f.write(line)
            process.wait()

        print(f"{Color.GREEN}✅ {tool} finished. Output saved to {file_path}.{Color.RESET}")

    except FileNotFoundError:
        print(f"{Color.RED}❌ '{tool}' not found! Install it or check your PATH.{Color.RESET}")
    except Exception as e:
        print(f"{Color.RED}❌ Error: {e}{Color.RESET}")

# === Run Selected Mode ===
def run_mode(choice, target):
    mode_name, tools = RECON_MODES[choice]
    clear()
    print(SEKIRO_BANNER)
    print(f"\n⚔  Starting {Color.CYAN}{mode_name}{Color.RESET} on: {Color.YELLOW}{target}{Color.RESET}")
    print("📦 Tools Loaded:\n")
    for tool in tools:
        print(f"   ➤ {tool}")
    print("\n🔄 Running tools...\n")

    for tool in tools:
        simulate_tool_run(tool, target)

    print(f"\n{Color.GREEN}✅ Recon complete for {target}.{Color.RESET}")
    print(f"📂 Output saved in: {Color.CYAN}output/{target}/<tool>/output_<timestamp>.txt{Color.RESET}\n")

# === Main ===
def main():
    while True:
        print_menu()
        try:
            choice = int(input("Select a mode (number): "))
            if choice == 0:
                print("\n👋 Exiting Sekiro. Stay stealthy, shinobi.")
                break
            if choice not in RECON_MODES:
                print("❌ Invalid mode.")
                time.sleep(1)
                continue

            target = input("\nEnter target (e.g. domain.com): ").strip()
            if not target:
                print("❌ Target cannot be empty.")
                time.sleep(1)
                continue

            run_mode(choice, target)
            input(f"\n🔁 {Color.YELLOW}Press Enter to return to main menu...{Color.RESET}")

        except KeyboardInterrupt:
            print(f"\n{Color.RED}👋 Exiting on keyboard interrupt.{Color.RESET}")
            break
        except ValueError:
            print("❌ Please enter a valid number.")
            time.sleep(1)

if __name__ == "__main__":
    main()
