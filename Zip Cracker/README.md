# Zip Brute-Force Password Cracker
*This script is a simple zip file password cracker that uses a brute-force technique to crack the password of a given zip file.*

## Usage
```
usage: zip-cracker.py [-h] zipfile wordlist
Brute force zip file password.

positional arguments:
  zipfile     path to zip file
  wordlist    path to wordlist file

optional arguments:
  -h, --help  show this help message and exit
```
*To run the script, simply provide the path to the zip file and the path to a wordlist file containing a list of potential passwords.*

## Dependencies
This script requires the following modules to be installed:

- zipfile
- argparse

*Both modules are included in the Python standard library, so no additional installation is needed.*

## How it works

*The script first reads in the wordlist file and stores each potential password as a list. It then attempts to extract the contents of the zip file using each password in the list until the correct password is found.

If the password is found, the script prints the password to the console and `returns True`. If the password is not found, the script `returns False`.*

## Limitations
*This script is a simple brute-force password cracker and may not be effective against complex passwords. Additionally, attempting to crack a password-protected zip file without permission is illegal and could result in serious consequences.*