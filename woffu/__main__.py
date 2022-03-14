import sys
from .woffu import Woffu
from .credentials import load_credentials
import argparse


print("Woffu Autologin Script\n")

has_saved_credentials, username, password = load_credentials()

if not has_saved_credentials:
    print(f"No credentials found")
    sys.exit(1)

woffunator = Woffu(username, password)
if not woffunator.is_working_day_for_me():
    print("Not a working day. Enjoy!")
    sys.exit(0)

parser = argparse.ArgumentParser()
parser.add_argument("cmd", help="", choices=["login", "logout"])
args = parser.parse_args()

try:
    if args["cmd"] == "login":
        woffunator.sign_in()
        print("Logged in!")
    elif args["cmd"] == "logout":
        raise NotImplementedError("logout")
        print("Logged out!")
    else:
        print(f"Unknown command: {args['cmd']}")
        sys.exit(1)
except Exception as e:
    print(f"Something went wrong when trying to log you in/out: {e.message}")
    sys.exit(1)
