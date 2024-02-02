#sublister.py
# code executed with -s flag
import os
import requests

def ezsub_lister(domain):
    #by default we use the 100 worldlist 

    print("\nStarting subdomain listing for:", domain)
    print("You chose the sublister option.\n")

    wordlist= os.path.join("subdomain_wordlists", "subdomains-100.txt")


    print("Choose a wordlist or press Enter to use the default one:")
    choice = input(" 0: 100 wordlist (default)\n 1: 500 wordlist\n 2: 1000 wordlist\nYour choice: ")

    match choice:
        case '0':
            print("you will use the 100 wordlist")
            wordlist=os.path.join("subdomain_wordlists", "subdomains-100.txt")
        case '1':
            print("you will use the 500 wordlist")
            os.path.join("subdomain_wordlists", "subdomains-500.txt")
        case '2':
            print("you will use the 1000 wordlist")
            os.path.join("subdomain_wordlists", "subdomains-1000.txt")
        case _:
            print("Invalid choice, using the 100 wordlist")
            os.path.join("subdomain_wordlists", "subdomains-100.txt")

    
    try:
        with open(wordlist, 'r') as file:
            sub_wordlist = file.read()
    except FileNotFoundError:
        print(f"Error: The wordlist file '{wordlist}' was not found.")
        return
    
    sub_wordlist=open(wordlist).read()
    subdomains=sub_wordlist.splitlines()

    print("\nScanning for valid subdomains...\n")
    found_subdomains = []
    for sub in subdomains:
        url=f"http://{sub}.{domain}"
        
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            found_subdomains.append(url)
            print("Valid domain: ", url)

    print("\nSubdomain listing completed.")
    if found_subdomains:
        print(f"Found {len(found_subdomains)} valid subdomains for {domain}:")
    else:
        print(f"No valid subdomains found for {domain}.")
