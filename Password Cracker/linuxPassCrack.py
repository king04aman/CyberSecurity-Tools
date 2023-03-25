import crypt


def find_password(filename, hash_val):
    with open(filename, 'r') as password_file:
        for passwd in password_file:
            passwd = passwd.strip()  # Strip new line characters
            hashed_passwd = crypt.crypt(passwd, hash_val)
            if hashed_passwd == hash_val:
                print("Password found: ", passwd)
                return passwd
    print("Password not found in the provided file.")
    return None


if __name__ == '__main__':
    hash_val = "$6$8HOLitkI$9HECw2MBzISI1O.RoyJdfugy4VHsTOU4RDTewcFECnZdWLpmtVwNo5a1/hg2kw4Qu74F08eMEwpLdK1eovfEd/"
    filename = "password.txt"
    find_password(filename, hash_val)
