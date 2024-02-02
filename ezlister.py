#ezlister.py
import argparse
import sys
import pyfiglet

from sublister import ezsub_lister 
from dirlister import ezdir_lister 



def main():
    title_text = "EzLister"
    ascii_art_title = pyfiglet.figlet_format(title_text, font="slant")
    
    welcome_message = "Welcome to EzLister!"
    description = "A simple tool for listing directories and subdomains."
    github_message = "Don't forget to give our GitHub a visit!"

    print(ascii_art_title)
    

    print("*" * len(welcome_message))
    print(welcome_message)
    print("*" * len(welcome_message))
    print()  
    
 
    print(description)
    print()  
    

    print(github_message)
    print("GitHub URL: https://github.com/yhabib05/ezlister")
    print()  

    parser = argparse.ArgumentParser(description="EZLister for directory and subdomain listing")
    parser.add_argument('domain', type=str, help="The domain to scan")
    parser.add_argument('-d', '--directory', action='store_true', help="Use directory lister")
    parser.add_argument('-s', '--subdomain', action='store_true', help="Use subdomain lister")
    parser.add_argument('-o', '--output', type=str, help="Output to a specified file")
    args = parser.parse_args()
    
    file_output=None

    if(args.directory):
        ezdir_lister(args.domain)
    
    if(args.subdomain):
        ezsub_lister(args.domain)
    
    if(args.output):
        with open(args.output, 'w') as file_output:
            sys.stdout = file_output # Redirect stdout to the output file


if __name__ == "__main__":
    main()