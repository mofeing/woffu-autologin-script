import sys
from .woffu import Woffu
from .credentials import load_credentials


print("Woffu Autologin Script\n")

has_saved_credentials, username, password = load_credentials()

if not has_saved_credentials:
    print(f"No credentials found")
    sys.exit(1)

woffunator = Woffu(username, password)
if not woffunator.is_working_day_for_me():
    print("Not a working day. Enjoy!")
    sys.exit(0)

try:
    woffunator.sign_in()
    print("Success!")
except Exception as e:
    print(f"Something went wrong when trying to log you in/out: {e.message}")
    sys.exit(1)
