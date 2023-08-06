from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GoogleDriveUploader:
    def __init__(self, playlists, music_root_path):
        self.playlists = playlists
        self.music_root_path = music_root_path

    def initialize(self):
        gauth = GoogleAuth()           
        self.drive = GoogleDrive(gauth)


# def create_folder(self, folderName):
#         file_metadata = {
#             'title': folderName,
#             'parents': [{'id': self.folder_id}], #parent folder
#             'mimeType': 'application/vnd.google-apps.folder'
#         }

#         folder = self.drive.CreateFile(file_metadata)
#         folder.Upload()