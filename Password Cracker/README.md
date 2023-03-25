# Password Cracker

*This script helps you to crack the password for the given hash value using a provided password file.*

## Requirements

- Python 3.x

## Usage

- Open the terminal and navigate to the directory where the script is located.
- Type python password_cracker.py to run the script.
- The script will output the password if it finds a match in the password file. If it does not find the password, it will print "Password not found in the provided file."

## Inputs
The script requires the following inputs:

- hash_val: The hash value for which the password is to be cracked.
- filename: The name of the file containing the list of passwords to be checked.

## Outputs
*If the password is found in the password file, the script will print "Password found: <password>". If the password is not found, it will print "Password not found in the provided file."*