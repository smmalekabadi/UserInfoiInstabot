#!/usr/bin/env python
import os
import sys
import getpass

SECRET_FILE = "secret.txt"


def add_credentials():
    with open(SECRET_FILE, "a") as f:
        print("Enter your login: ")
        f.write(str(sys.stdin.readline().strip()) + ":")
        print("Enter your password: ")
        f.write(getpass.getpass() + "\n")


def get_credentials(username=None):
    "Returns login and password stored in SECRET_FILE"
    while not check_secret():
        pass
    while True:
        with open(SECRET_FILE, "r") as f:
            lines = [line.strip().split(":", 2) for line in f.readlines()]
        if username is not None:
            for login, password in lines:
                if login == username.strip():
                    return login, password
        print("Which account do you want to use? (Type number)")
        for ind, (login, password) in enumerate(lines):
            print("%d: %s" % (ind + 1, login))
        print("%d: %s" % (0, "add another account."))
        print("%d: %s" % (-1, "delete all accounts."))
        try:
            ind = int(sys.stdin.readline())
            if ind == 0:
                add_credentials()
                continue
            if ind == -1:
                delete_credentials()
                check_secret()
                continue
            if ind - 1 in list(range(len(lines))):
                return lines[ind - 1]
        except:
            print("Wrong input. I need the number of account to use.")


def check_secret():
    while True:
        if os.path.exists(SECRET_FILE):
            with open(SECRET_FILE, "r") as f:
                try:
                    login, password = f.readline().strip().split(":")
                    if len(login) < 4 or len(password) < 6:

                        print("Data in 'secret.txt' file is invalid. "
                              "We will delete it and try again.")

                        os.remove(SECRET_FILE)
                    else:
                        return True
                except:
                    print("Your file is broken. We will delete it "
                          "and try again.")
                    os.remove(SECRET_FILE)
        else:
            print("We need to create a text file '%s' where "
                  "we will store your login and password from Instagram." % SECRET_FILE)
            print("Don't worry. It will be stored locally.")
            while True:
                add_credentials()
                print("Do you want to add another account? (y/n)")
                if "y" not in sys.stdin.readline():
                    break


def delete_credentials():
    if os.path.exists(SECRET_FILE):
        os.remove(SECRET_FILE)


if __name__ == "__main__":
    check_secret()
