import zipfile
import argparse


def extract_zip(zipfile_path, password):
    try:
        with zipfile.ZipFile(zipfile_path) as zip_file:
            zip_file.extractall(pwd=password.encode())
            print("Password found: " + password)
            return True

    except Exception as e:
        if "Bad password" in str(e):
            print("Incorrect password: " + password)
        else:
            print("Error occurred: " + str(e))

    return False


def brute_force(zipfile_path, password_list):
    for password in password_list:
        if extract_zip(zipfile_path, password):
            break


def main():
    parser = argparse.ArgumentParser(
        description="Brute force zip file password.")
    parser.add_argument("zipfile", metavar="zipfile",
                        type=str, help="path to zip file")
    parser.add_argument("wordlist", metavar="wordlist",
                        type=str, help="path to wordlist file")
    args = parser.parse_args()

    with open(args.wordlist, "r") as f:
        password_list = f.read().splitlines()

    brute_force(args.zipfile, password_list)


if __name__ == "__main__":
    main()
