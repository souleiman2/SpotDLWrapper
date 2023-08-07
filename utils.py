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

def added_diff(old : list, new : list):
    old.sort()
    new.sort()
    
    diff = []
    index_old, index_new = 0, 0
    while index_old < len(old) and index_new < len(new):
        if old[index_old] == new[index_new]:
            index_old += 1
            index_new += 1
        elif new[index_new] < old[index_old]:
            diff.append(new[index_new])
            index_new += 1
        else:
            index_old += 1
    
    if index_new < len(new):
        diff += new[index_new:]
    
    return diff
    