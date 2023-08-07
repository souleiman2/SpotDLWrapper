from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import os
from utils import read_txt, name_to_path


class GoogleDriveUploader:
    def __init__(self, playlists, music_root_path):
        self.playlists = playlists
        self.music_root_path = music_root_path
        self.initialize()
        
    def initialize(self):
        gauth = GoogleAuth()
        self.drive = GoogleDrive(gauth)

    def currently_uploaded_songs(self, parent_folder_id):
        file_name = 'music_list.txt'
        query = f"'{parent_folder_id}' in parents and title='{file_name}' and trashed=false"
        file_list = self.drive.ListFile({'q': query}).GetList()
        
        if len(file_list) > 0:
            # The file exists, you can proceed to read its content.
            file1 = file_list[0]
            content = file1.GetContentString()
            return content
        return None
        
        
    def upload_new_current_songs(self, folder_id, content):
        file_name = 'music_list.txt'
        query = f"'{folder_id}' in parents and title='{file_name}' and trashed=false"
        file_list = self.drive.ListFile({'q': query}).GetList()
        
        if len(file_list) > 0:
            # The file exists, you can proceed to read its content.
            file1 = file_list[0]
            file1.SetContentString(content)
            file1.Upload()
        else:
            file1 = self.drive.CreateFile({'parents': [{'id': folder_id}],'title': 'music_list.txt'})  
            # Set content of the file from the given string.
            file1.SetContentString(content) 
            file1.Upload()
        return None
            
            
        
        
        # Create a GoogleDriveFile instance with title 'test.txt'.
        file1 = self.drive.CreateFile({'parents': [{'id': folder_id}],'title': 'music_list.txt'})  
        # Set content of the file from the given string.
        file1.SetContentString(content) 
        file1.Upload()
        
    
    
    def update_playlist(self, playlist):
        convert_full_path = lambda name : os.path.join(name_to_path(self.music_root_path, playlist["name"]), name)
        upload_file_list = list(map(lambda x : x.strip(), read_txt(convert_full_path("music_list.txt"))))
        
        for upload_file in upload_file_list:
            gfile = self.drive.CreateFile({'parents': [{'id': playlist["google_drive_folder_id"]}], 'title': upload_file})
            # Read file and set it as the content of this instance.
            gfile.SetContentFile(convert_full_path(upload_file))
            gfile.Upload() # Upload the file.

    def update_all_playlists(self):
        # checks for any playlist not containing a google_drive_folder_id
        index = 0
        while index < len(self.playlists):
            if "google_drive_folder_id" not in self.playlists[index]:
                print("Error ! You are trying to upload the playlists to your google drive, but one is missing the google_drive_folder_id : ", str(playlist))
                exit()
            index += 1
            
        for playlist in self.playlists:
            self.update_playlist(playlist)
            
if __name__ == "__main__":
    google_driver = GoogleDriveUploader(None, None)
    google_driver.upload_new_current_songs("1oFqwgXpmgWL2EF3Rn-CVzuckFneVBFby", "Hello world 2!")
    # google_driver.currently_uploaded_songs("1oFqwgXpmgWL2EF3Rn-CVzuckFneVBFby")