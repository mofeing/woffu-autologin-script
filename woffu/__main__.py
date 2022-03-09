import sys
from .woffu import Woffu
from .credentials import load_credentials, default_credentials_paths


print("Woffu Autologin Script\n")

has_saved_credentials, username, password = load_credentials()

woffunator = Woffu(username, password)
if woffunator.is_working_day_for_me():
    try:
        woffunator.sign_in()
        print("Success!")
    except Exception as e:
        print(f"Something went wrong when trying to log you in/out: {e.message}")
        sys.exit(1)
else:
    print("Not a working day. Enjoy!")

if not has_saved_credentials:
    credentials_path = default_credentials_paths()[0]
    print(f"Saving credentials to file {credentials_path}")
    woffunator.save_data(credentials_path)
