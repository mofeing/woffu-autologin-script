import getpass
import json
from pathlib import Path
from operator import itemgetter
import os.path

CREDENTIALS_FILENAME = ".woffu-autologin-script.json"
LEGACY_CREDENTIALS_FILENAME = "data.json"


def load_credentials():
    credential_paths = default_credentials_paths()
    for credentials_file in credential_paths:
        if not os.path.exists(credentials_file):
            continue

        try:
            print(f"Using credentials from {credentials_file}")
            with open(credentials_file, "r") as json_data:
                login_info = json.load(json_data)
                username, password = itemgetter(
                    "username",
                    "password",
                )(login_info)

            return True, username, password

        except (OSError, IOError, json.JSONDecodeError):
            pass

    # Ask for user input if there are no credential files created
    username = input("Enter your Woffu username:\n")
    password = getpass.getpass("Enter your password:\n")

    return False, username, password


def default_credentials_paths():
    credential_files = [CREDENTIALS_FILENAME, LEGACY_CREDENTIALS_FILENAME]
    credential_folders = [Path.home(), "."]
    credential_paths = [os.path.join(d, f) for f in credential_files for d in credential_folders]
    return credential_paths
