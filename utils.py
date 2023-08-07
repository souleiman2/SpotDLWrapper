import os
import json

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def read_txt(path):
    with open(path) as f:
        return f.readlines()

def name_to_path(root_folder, name):
    format_name = lambda string : '_'.join(string.lower().strip().split(" "))
    return os.path.join(root_folder, format_name(name))
