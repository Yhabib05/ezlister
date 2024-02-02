#dirlister.py
# code executed with -d flag
import os
import requests

def ezdir_lister(domain):

    choice= input("\n Choose your own wordlist here or skip this to use the default one :")
    wordlist=None

    if(choice):
        wordlist=choice
        print("You will use your own wordlist")
    else:
         wordlist= os.path.join( "directory_wordlists", "dsstorewordlist.txt")
         print("We will be using the default wordlist: dsstorewordlist.txt \n That was taken from the famous github https://github.com/aels/subdirectories-discover/tree/main ")


    dir_wordlist=open(wordlist).read()
    directories=dir_wordlist.splitlines()

    found_directories=[]
    for dir in directories:
        url=f"http://{domain}/{dir}.html"
        
        request=requests.get(url)
        if(request.status_code==404):
            pass     
        else:
            found_directories.append(dir)
            print("Valid directory: ", dir)
       
    print("\nDirectories listing completed.")
    if found_directories:
        print(f"Found {len(found_directories)} valid directories for {domain}")
    else:
        print(f"No valid directories found for {domain}.")