#You will not be able to run this file here and will need to copy it onto your computer and run it on your machine.
#You will also need to make sure you have installed the requests module from PyPi (pip install)
#References for modules below:
#https://api.pwnedpasswords.com/range/ is the repository that contains all hacked passwords
#https://passwordsgenerator.net/sha1-hash-generator/    SHA1 Hash Generation. We wil be using the hashlib
import requests
import hashlib
import sys

def request_api_data(query_char):           #Standard boiler plate to check if url is valid
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:              #Check if response Code is valid
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):        #Define function that checks if entered password is part of compromised ones returned from API
    hashes = (line.split(':') for line in hashes.text.splitlines())         #Convert into generator expression. Note, we have to use splitlines here. Read more about it
    for h, count in hashes:                                                 #Loop through for value and count
        if h == hash_to_check:                                              #Returns count
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()       #Encode the password in sha1
    first5_char, tail = sha1password[:5], sha1password[5:]                    #Slice the first 5 characters and remaining characters into 2 variables
    response = request_api_data(first5_char)                                #First 5 characters is only used to pass into API
    return get_password_leaks_count(response, tail)                         #Returns function that is defined above

def main():                                                             #Run Code
    print("Let's see if your password is Safe!!\n")
    password = input("Enter the password you will like to check: ")
    count = pwned_api_check(password)
    if count:
        print(f'{password} was found {count} times... you should probably change your password!')
    else:
        print(f'{password} was NOT found. Carry on!')
        return 'done!'

if __name__ == '__main__':
    main()