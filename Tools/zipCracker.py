import zipfile
from typing import Iterable
from os.path import isfile

ZIP_FILENAME = "test.zip"
PASSWORDS_FILENAME = "password.txt"


def generate_numeral_passwords(num_digits: int):
    min_number = 0
    max_number = 10 ** num_digits
    for password in range(min_number, max_number):
        yield str(password)


def extract_zip_with_passwords(zip_object: zipfile.ZipFile, passwords: Iterable[str]):
    for password in passwords:
        try:
            print("Trying:", password)
            zip_object.extractall(pwd=password.encode('ascii'))
            print("Password Found:", password, "  <<<<<<<<<<")
            return True

        except (RuntimeError, zipfile.BadZipFile):
            # wrong password
            pass

    # all passwords failed
    return False


def main():
    zip_object = zipfile.ZipFile(ZIP_FILENAME)

    if isfile(PASSWORDS_FILENAME):
        with open(PASSWORDS_FILENAME, 'r') as f:
            passwords = f.read().splitlines()

        if extract_zip_with_passwords(zip_object, passwords):
            return

        print()
        print("password not found in", PASSWORDS_FILENAME)
    else:
        print(PASSWORDS_FILENAME, "is not a valid file.")

    num_digits = 3
    numeral_passwords = generate_numeral_passwords(num_digits=num_digits)
    print("trying numbers with", num_digits, "digits:")
    if extract_zip_with_passwords(zip_object, numeral_passwords):
        return

    print("all passwords failed.")


if __name__ == "__main__":
    main()
