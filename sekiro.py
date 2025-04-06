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
███████╗███████╗██╗  ██╗██╗██╗██████╗  ██████╗ 
██╔════╝██╔════╝╚██╗██╔╝██║██║██╔══██╗██╔═══██╗
███████╗█████╗   ███╔╝  ██║██║██████╔╝██║   ██║
╚════██║██╔══╝   ██╔██╗ ██║██║██╔═══╝ ██║   ██║
███████║███████╗██╔╝ ██╗██║██║██║     ╚██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝      ╚═════╝  

         Sekiro Recon Framework
       Developed by Vignesh (chip)
------------------------------------------------
"""

# === Recon Categories ===
RECON_MODES = {
    1: ("Passive Recon", [
        "subfinder", "assetfinder", "amass_passive", "sublist3r"
    ]),
    2: ("Deep Recon", [
        "waybackurls", "katana", "gau", "hakrawler"
    ]),
    3: ("DNS Recon", [
        "dnsrecon", "dnsenum", "dnsmap", "dig", "fierce"
    ])
}

# === Tool Command Mappings ===
TOOL_COMMANDS = {
    "subfinder": ["subfinder", "-d"],
    "assetfinder": ["assetfinder"],
    "amass_passive": ["amass", "enum", "-passive", "-d"],
    "sublist3r": ["sublist3r", "-d"],
    "waybackurls": ["waybackurls"],
    "katana": ["katana", "-u", "http://{}"],
    "gau": ["gau"],
    "hakrawler": ["hakrawler", "-url", "http://{}"],
    "dnsrecon": ["dnsrecon", "-d"],
    "dnsenum": ["dnsenum"],
    "dnsmap": ["dnsmap"],
    "dig": ["dig"],
    "fierce": ["fierce", "--domain"]
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

# === Tool Execution ===
def simulate_tool_run(tool, target):
    print(f"\n{Color.CYAN}▶ Running {tool} on {target}...{Color.RESET}")

    clean_target = target.replace("https://", "").replace("http://", "").strip("/")
    output_dir = f"output/{clean_target}"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{output_dir}/{tool}_{timestamp}.txt"

    cmd = TOOL_COMMANDS.get(tool)
    if not cmd:
        print(f"{Color.RED}❌ Tool '{tool}' not configured.{Color.RESET}")
        return

    if "{}" in " ".join(cmd):
        cmd = [arg.format(target) if "{}" in arg else arg for arg in cmd]
    else:
        cmd.append(target)

    try:
        with open(file_path, "w") as f:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(f"{Color.YELLOW}{line.strip()}{Color.RESET}")
                f.write(line)
            process.wait()

        print(f"{Color.GREEN}✅ {tool} finished. Output saved to {file_path}.{Color.RESET}")

    except FileNotFoundError:
        print(f"{Color.RED}❌ '{tool}' not found! Install or add to PATH.{Color.RESET}")
    except Exception as e:
        print(f"{Color.RED}❌ Error: {e}{Color.RESET}")

# === Run Mode ===
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
    print(f"📂 Output saved in: {Color.CYAN}output/{target}/\n{Color.RESET}")

# === Main Loop ===
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
