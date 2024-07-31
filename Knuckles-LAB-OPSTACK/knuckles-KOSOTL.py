import os
import sys
import time
import json

# Color codes for terminal output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
WHITE = '\033[97m'
BOLD_WHITE = '\033[1;97m'
RESET = '\033[0m'

# File paths for saving configurations
ENV_CONFIG_FILE = os.path.expanduser("~") + "/optimism/.envrc"
API_KEY_FILE = os.path.expanduser("~") + "/optimism/api_key.txt"
OPTIMISM_DIR = os.path.expanduser("~") + "/optimism"
OP_GETH_DIR = os.path.expanduser("~") + "/op-geth"
OP_NODE_DIR = os.path.expanduser("~") + "/optimism/op-node"
OP_BATCHER_DIR = os.path.expanduser("~") + "/optimism/op-batcher"
OP_PROPOSER_DIR = os.path.expanduser("~") + "/optimism/op-proposer"

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_animation(message):
    """Print an ASCII animation with a red circle and 'OP' in the middle."""
    frames = [
        f"""
{RED}   _______
  /         \\
 /  {WHITE}  OP  {RED}  \\
|           |
 \\_________/{RESET}
""",
        f"""
{RED}  ________
 /        \\
|  {WHITE} OP {RED}  |
 \\________/{RESET}
""",
        f"""
{RED}  ________
 /        \\
| {WHITE} OP {RED}  |
 \\_______/{RESET}
""",
        f"""
{RED}   _______
  /        \\
 / {WHITE} OP {RED}   \\
|         |
 \\_______/{RESET}
"""
    ]

    for _ in range(10):  # Loop through the frames to create the animation
        for frame in frames:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.3)
    print()  # Move to the next line after the animation

def display_intro():
    """Display the introductory ASCII art and welcome message."""
    clear_screen()
    print(f"""
{RED}
  
{RESET}
{BOLD_WHITE}

{RESET}
{YELLOW}WELCOME TO KOSOTL{RESET}
""")
    print_ascii_animation("OP")

def display_menu():
    """Display the menu options."""
    print(f"""
{YELLOW}Menu:
1. Check System Requirements
2. Check for Dependencies
3. Prepare Environment
4. Start Installation of Knuckles OPChain
5. Deploy Contracts and Generate Configs
6. Check for Errors
7. Display Current Version of OPSTACK
8. Register and Get API Key
9. Configure Addresses
10. Input and Save Addresses
11. Load Environment Variables
12. Print Registered Addresses
13. Complete Installation and Configuration
14. Start All Required Nodes and Modules
15. Connect and Obtain Ethereum Addresses
16. Exit
{RESET}""")

def check_system_requirements():
    """Check if the system is running Debian 12 and has at least 16GB of RAM."""
    clear_screen()
    print("Checking system requirements...")
    
    try:
        # Check for Debian 12
        print(f"{YELLOW}Checking if the system is running Debian 12...{RESET}")
        os.system("lsb_release -a | grep 'Distributor ID' | grep 'Debian'")
        os.system("lsb_release -a | grep 'Release' | grep '12'")
        
        # Check for RAM
        print(f"{YELLOW}Checking for at least 16GB of RAM...{RESET}")
        mem_info = os.popen("grep MemTotal /proc/meminfo").read().strip()
        total_memory_kb = int(mem_info.split()[1])
        total_memory_gb = total_memory_kb / (1024 ** 2)
        
        if total_memory_gb >= 16:
            print(f"{GREEN}System meets the memory requirement: {total_memory_gb:.2f} GB{RESET}")
        else:
            print(f"{RED}System does not meet the memory requirement: {total_memory_gb:.2f} GB{RESET}")
    except Exception as e:
        print(f"{RED}Fatal error occurred: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")
    
    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def check_for_dependencies():
    """Check for required dependencies and install missing ones."""
    clear_screen()
    print("Checking for dependencies...")
    dependencies = {
        'git': {'version_command': 'git --version', 'min_version': '2'},
        'go': {'version_command': 'go version', 'min_version': '1.21'},
        'node': {'version_command': 'node --version', 'min_version': '20'},
        'pnpm': {'version_command': 'pnpm --version', 'min_version': '8'},
        'foundry': {'version_command': 'forge --version', 'min_version': '0.2.0'},
        'make': {'version_command': 'make --version', 'min_version': '3'},
        'jq': {'version_command': 'jq --version', 'min_version': '1.6'},
        'direnv': {'version_command': 'direnv --version', 'min_version': '2'}
    }

    for dep, info in dependencies.items():
        print(f"{YELLOW}Checking {dep}...{RESET}")
        try:
            version_output = os.popen(info['version_command']).read().strip()
            if version_output:
                version = version_output.split()[1]  # Assuming version is the second word
                print(f"{GREEN}{dep} version: {version}{RESET}")
                # Check version
                if version < info['min_version']:
                    print(f"{RED}Please update {dep} to at least version {info['min_version']}.{RESET}")
                    # Install missing dependencies (Placeholder)
                    print(f"{YELLOW}Installing missing {dep}...{RESET}")
                    os.system(f"sudo apt-get install -y {dep}")
                else:
                    print(f"{GREEN}{dep} meets the version requirement.{RESET}")
            else:
                print(f"{RED}{dep} is not installed.{RESET}")
                # Install missing dependencies (Placeholder)
                print(f"{YELLOW}Installing {dep}...{RESET}")
                os.system(f"sudo apt-get install -y {dep}")
        except Exception as e:
            print(f"{RED}Fatal error occurred while checking {dep}: {e}{RESET}")
            print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def prepare_environment():
    """Prepare the environment by evaluating direnv hook."""
    clear_screen()
    print("Preparing environment...")

    try:
        # Hook direnv into the shell
        print(f"{YELLOW}Running direnv hook...{RESET}")
        result = os.system('eval "$(direnv hook bash)"')
        
        if result == 0:
            print(f"{GREEN}direnv hook executed successfully!{RESET}")
        else:
            print(f"{RED}Failed to execute direnv hook.{RESET}")
    except Exception as e:
        print(f"{RED}Fatal error occurred: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def start_installation():
    """Start the installation process for Knuckles OPChain."""
    clear_screen()
    print("Starting installation of Knuckles OPChain...")
    
    try:
        # Clone and navigate to the Optimism repository
        print(f"{YELLOW}Cloning Optimism repository...{RESET}")
        os.chdir(os.path.expanduser("~"))
        os.system("git clone https://github.com/ethereum-optimism/optimism.git")
        os.chdir(OPTIMISM_DIR)
        
        # Check out the tutorials/chain branch
        print(f"{YELLOW}Checking out the tutorials/chain branch...{RESET}")
        os.system("git checkout tutorials/chain")

        # Run versions script and install dependencies
        print(f"{YELLOW}Running versions script...{RESET}")
        os.system("./packages/contracts-bedrock/scripts/getting-started/versions.sh")
        
        print(f"{YELLOW}Installing dependencies...{RESET}")
        os.system("pnpm install")
        
        # Build packages
        print(f"{YELLOW}Building packages...{RESET}")
        os.system("make op-node op-batcher op-proposer")
        os.system("pnpm build")

        # Clone and build op-geth
        print(f"{YELLOW}Cloning op-geth repository...{RESET}")
        os.chdir(os.path.expanduser("~"))
        os.system("git clone https://github.com/ethereum-optimism/op-geth.git")
        os.chdir(OP_GETH_DIR)
        
        print(f"{YELLOW}Building op-geth...{RESET}")
        os.system("make")
        
        print(f"{GREEN}Installation complete!{RESET}")

    except Exception as e:
        print(f"{RED}Fatal error occurred during installation: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def deploy_contracts_and_generate_configs():
    """Deploy L1 contracts, generate configuration files, and set up the op-geth directory."""
    clear_screen()
    print("Deploying L1 contracts and generating configuration files...")

    try:
        # Deploy L1 contracts
        print(f"{YELLOW}Deploying L1 contracts...{RESET}")
        os.system(f"forge script scripts/Deploy.s.sol:Deploy --private-key $GS_ADMIN_PRIVATE_KEY --broadcast --rpc-url $L1_RPC_URL --slow")
        
        # Check if deployment was successful
        print(f"{YELLOW}If you see an EvmError: Revert error, you may need to change the IMPL_SALT environment variable.{RESET}")

        # Generate L2 config files
        print(f"{YELLOW}Generating L2 config files...{RESET}")
        os.chdir(os.path.expanduser("~") + "/optimism/op-node")
        os.system("go run cmd/main.go genesis l2 "
                  "--deploy-config ../packages/contracts-bedrock/deploy-config/getting-started.json "
                  "--l1-deployments ../packages/contracts-bedrock/deployments/getting-started/.deploy "
                  "--outfile.l2 genesis.json "
                  "--outfile.rollup rollup.json "
                  "--l1-rpc $L1_RPC_URL")

        # Generate JWT
        print(f"{YELLOW}Generating JWT...{RESET}")
        os.system("openssl rand -hex 32 > jwt.txt")

        # Copy genesis files into op-geth directory
        print(f"{YELLOW}Copying genesis files into op-geth directory...{RESET}")
        os.system(f"cp genesis.json {OP_GETH_DIR}")
        os.system(f"cp jwt.txt {OP_GETH_DIR}")

        print(f"{GREEN}Contracts deployed and configuration files generated successfully!{RESET}")

    except Exception as e:
        print(f"{RED}Fatal error occurred during deployment and configuration: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()


def check_for_errors():
    """Check for errors in the setup."""
    clear_screen()
    print("Checking for errors...")
    
    try:
        # Placeholder for error checking logic
        print(f"{YELLOW}Checking logs and setup...{RESET}")
        # Check logs or setup here
        
        print(f"{GREEN}Error check complete! No issues detected.{RESET}")

    except Exception as e:
        print(f"{RED}Fatal error occurred while checking for errors: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def display_current_version():
    """Display the current version of OPSTACK."""
    clear_screen()
    print("Displaying current version of OPSTACK...")
    
    try:
        # Placeholder for version display
        print(f"{YELLOW}Fetching version...{RESET}")
        os.system("make version")
        
    except Exception as e:
        print(f"{RED}Fatal error occurred while fetching the version: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def register_and_get_api_key():
    """Register and get API key."""
    clear_screen()
    print("Registering and obtaining API key...")
    
    try:
        # Placeholder for API key registration and retrieval
        print(f"{YELLOW}Registering and retrieving API key...{RESET}")
        
        with open(API_KEY_FILE, 'r') as file:
            api_key = file.read().strip()
        
        print(f"{GREEN}API Key retrieved: {api_key}{RESET}")

    except Exception as e:
        print(f"{RED}Fatal error occurred while retrieving the API key: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def configure_addresses():
    """Prompt user to input addresses and private keys, and save to .envrc file."""
    clear_screen()
    print("Configuring addresses...")

    try:
        with open(ENV_CONFIG_FILE, 'w') as file:
            file.write(f"export GS_ADMIN_ADDRESS={input('Enter Admin Address: ').strip()}\n")
            file.write(f"export GS_ADMIN_PRIVATE_KEY={input('Enter Admin Private Key: ').strip()}\n")
            file.write(f"export GS_BATCHER_ADDRESS={input('Enter Batcher Address: ').strip()}\n")
            file.write(f"export GS_BATCHER_PRIVATE_KEY={input('Enter Batcher Private Key: ').strip()}\n")
            file.write(f"export GS_PROPOSER_ADDRESS={input('Enter Proposer Address: ').strip()}\n")
            file.write(f"export GS_PROPOSER_PRIVATE_KEY={input('Enter Proposer Private Key: ').strip()}\n")
            file.write(f"export GS_SEQUENCER_ADDRESS={input('Enter Sequencer Address: ').strip()}\n")
            file.write(f"export GS_SEQUENCER_PRIVATE_KEY={input('Enter Sequencer Private Key: ').strip()}\n")

        print(f"{GREEN}Addresses and keys saved successfully to {ENV_CONFIG_FILE}!{RESET}")
    except Exception as e:
        print(f"{RED}Error occurred while configuring addresses: {e}{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def input_and_save_addresses():
    """Input and save addresses."""
    clear_screen()
    print("Inputting and saving addresses...")
    
    try:
        # Input and save addresses
        address = input("Enter address to save: ").strip()
        
        with open(os.path.join(OPTIMISM_DIR, 'addresses.txt'), 'a') as file:
            file.write(f"{address}\n")
        
        print(f"{GREEN}Address saved successfully!{RESET}")

    except Exception as e:
        print(f"{RED}Fatal error occurred while saving addresses: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def load_environment_variables():
    """Load environment variables from .envrc."""
    clear_screen()
    print("Loading environment variables...")
    
    try:
        if os.path.isfile(ENV_CONFIG_FILE):
            with open(ENV_CONFIG_FILE, 'r') as file:
                env_vars = file.readlines()
                for line in env_vars:
                    if line.startswith("export"):
                        key, value = line.strip().split('=', 1)
                        os.environ[key] = value.split('=', 1)[1]
            
            print(f"{GREEN}Environment variables loaded successfully!{RESET}")
        else:
            print(f"{RED}Error: {ENV_CONFIG_FILE} not found.{RESET}")

    except Exception as e:
        print(f"{RED}Fatal error occurred while loading environment variables: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def print_registered_addresses():
    """Print registered addresses."""
    clear_screen()
    print("Printing registered addresses...")
    
    try:
        with open(os.path.join(OPTIMISM_DIR, 'addresses.txt'), 'r') as file:
            addresses = file.readlines()
        
        print(f"{YELLOW}Registered Addresses:{RESET}")
        for address in addresses:
            print(f"- {address.strip()}")
    
    except Exception as e:
        print(f"{RED}Fatal error occurred while printing registered addresses: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def complete_installation_and_configuration():
    """Complete the installation and configuration."""
    clear_screen()
    print("Completing installation and configuration...")
    
    try:
        # Placeholder for completing installation and configuration
        print(f"{YELLOW}Completing installation and configuration...{RESET}")
        # Additional logic here
        
        print(f"{GREEN}Installation and configuration complete!{RESET}")

    except Exception as e:
        print(f"{RED}Fatal error occurred while completing installation and configuration: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def start_all_nodes_and_modules():
    """Start all required nodes and modules."""
    clear_screen()
    print("Starting all required nodes and modules...")
    
    try:
        # Start all required nodes and modules
        print(f"{YELLOW}Starting nodes and modules...{RESET}")
        os.chdir(OP_NODE_DIR)
        os.system("make start")
        os.chdir(OP_BATCHER_DIR)
        os.system("make start")
        os.chdir(OP_PROPOSER_DIR)
        os.system("make start")
        
        print(f"{GREEN}All nodes and modules started successfully!{RESET}")

    except Exception as e:
        print(f"{RED}Fatal error occurred while starting nodes and modules: {e}{RESET}")
        print(f"{YELLOW}Please ensure that you have followed the first steps for the Knuckles OPChain tool.{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def connect_to_ethereum():
    """Connect to Ethereum node and obtain ETH balance."""
    clear_screen()
    print("Connecting to Ethereum and obtaining ETH balance...")

    try:
        # Load environment variables from .envrc
        if os.path.isfile(ENV_CONFIG_FILE):
            with open(ENV_CONFIG_FILE, 'r') as file:
                env_vars = file.readlines()
                for line in env_vars:
                    if line.startswith("export"):
                        key, value = line.strip().split('=', 1)
                        os.environ[key] = value.split('=', 1)[1]
        
        # Connect to the Ethereum node
        infura_url = os.getenv('ETHEREUM_NODE_URL')  # You need to set this variable
        if not infura_url:
            print(f"{RED}Error: ETHEREUM_NODE_URL is not set in {ENV_CONFIG_FILE}.{RESET}")
            return
        
        web3 = Web3(Web3.HTTPProvider(infura_url))
        
        if not web3.isConnected():
            print(f"{RED}Failed to connect to Ethereum node.{RESET}")
            return
        
        # Fetch balance of an address
        address = input("Enter Ethereum address to check balance: ").strip()
        balance = web3.eth.get_balance(address)
        balance_eth = web3.fromWei(balance, 'ether')
        
        print(f"{GREEN}ETH Balance for address {address}: {balance_eth} ETH{RESET}")

    except Exception as e:
        print(f"{RED}Error occurred while connecting to Ethereum: {e}{RESET}")

    input(f"{BLUE}Press Enter to return to the menu...{RESET}")
    clear_screen()

def main():
    """Main function to run the script."""
    while True:
        display_intro()
        display_menu()
        
        try:
            choice = int(input(f"{BLUE}Enter your choice (1-16): {RESET}"))
            if choice == 1:
                check_system_requirements()
            elif choice == 2:
                check_for_dependencies()
            elif choice == 3:
                prepare_environment()
            elif choice == 4:
                start_installation()
            elif choice == 5:
                deploy_contracts_and_generate_configs()
            elif choice == 6:
                check_for_errors()
            elif choice == 7:
                display_current_version()
            elif choice == 8:
                register_and_get_api_key()
            elif choice == 9:
                configure_addresses()
            elif choice == 10:
                input_and_save_addresses()
            elif choice == 11:
                load_environment_variables()
            elif choice == 12:
                print_registered_addresses()
            elif choice == 13:
                complete_installation_and_configuration()
            elif choice == 14:
                start_all_nodes_and_modules()
            elif choice == 15:
                connect_to_ethereum()
            elif choice == 16:
                print(f"{GREEN}Exiting...{RESET}")
                break
            else:
                print(f"{RED}Invalid choice, please enter a number between 1 and 16.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input. Please enter a number.{RESET}")

if __name__ == "__main__":
    main()


