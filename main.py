import os
import json

def read_csv(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def write_csv():
    pass

def update_playlist(root_folder, playlists):
    format_name = lambda string : '_'.join(string.lower().strip().split(" "))
    query_builder = lambda link, folder_path : "spotdl {} --output {}".format(link, folder_path)
    for elem in playlists:
        folder_path = os.path.join(root_folder, format_name(elem["name"]))
        os.system(query_builder(elem["link"], folder_path))
        os.system("ls {} | sed s/^.*\\/\// > {}".format(os.path.join(folder_path, "*.mp3"), os.path.join(folder_path, "music_list.txt")))


print("For the playlist list you can update the list manually.")

val = None
while val not in ["1","2","3"]:
    val = input("""Press either 1, 2 or 3:
    - 1 for updating the playlists locally
    - 2 for updating the playlists online
    - 3 for updating both (locally then online)
    - 4 to cancel and stop""")
val = int(val)


if val != 4:
    data = read_csv("playlists.json")
    root_folder, playlists = data["root_folder"], data["playlists"]

    if val == 1 or val == 3:
        # update the local list of music
        update_playlist(root_folder, playlists)
    
    if val == 2 or val == 3:
        # update the online list of music
        google_driver = GoogleDriveUploader()
        google_driver.upload()
else:
    exit()













