import os
from utils import read_json, name_to_path
from google_drive_uploader import GoogleDriveUploader

def update_playlist(root_folder, playlists):
    query_builder = lambda link, folder_path : f"spotdl {link} --output {folder_path}"
    for elem in playlists:
        folder_path = name_to_path(root_folder, elem["name"])
        os.system(query_builder(elem["link"], folder_path))
        os.system(f"ls {os.path.join(folder_path, '*.mp3')} | sed 's#^.*/##' > {os.path.join(folder_path, 'music_list.txt')}")

print("For the playlist list you can update the list manually.")

val = None
while val not in ["1","2","3"]:
    val = input("""Press either 1, 2 or 3:
    - 1 for updating the playlists locally
    - 2 for updating the playlists online (from the local version)
    - 3 for updating both (locally then online)
    - 4 to cancel and stop

    Enter you answer :""")

val = int(val)


if val != 4:
    data = read_json("playlists.json")
    root_folder, playlists = data["root_folder"], data["playlists"]

    if val == 1 or val == 3:
        # update the local list of music
        update_playlist(root_folder, playlists)
    
    if val == 2 or val == 3:
        # update the online list of music
        google_driver = GoogleDriveUploader(playlists, root_folder)
        google_driver.update_all_playlists()
else:
    exit()

