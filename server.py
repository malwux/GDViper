from flask import Flask, request
import os

app = Flask(__name__)

# Base folder is current working directory
BASE_FOLDER = os.getcwd()
print(f"[+] Files will be saved in: {BASE_FOLDER}")

@app.route("/upload", methods=["POST"])
def upload_file():
    """Receive any file and save it in the current folder."""
    try:
        if not request.files:
            return "No files received", 400

        for key, file in request.files.items():
            save_path = os.path.join(BASE_FOLDER, file.filename)
            file.save(save_path)
            print(f"[+] Saved file: {save_path}")

        return "Files saved successfully", 200

    except Exception as e:
        print(f"[-] Error saving files: {e}")
        return f"Error: {e}", 500

@app.route("/", methods=["GET"])
def index():
    return f"Flask server running. Files will be saved in {BASE_FOLDER}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
