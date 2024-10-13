import os

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive


drive = authenticate_drive()


def upload_file(file_path):
    file = drive.CreateFile({'title': os.path.basename(file_path)})
    file.SetContentFile(file_path)
    file.Upload()
    return file['id']


def upload_to_google_drive():
    audio = "example_data/audio.wav"
    audio_link = upload_file(audio)

    script = "example_data/script.json"
    script_link = upload_file(script)

    print("Audio Link:", audio_link)
    print("Script Link:", script_link)
