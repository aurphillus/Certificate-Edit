import os
from os import listdir
from os.path import isfile, join
import requests


def load_files(parent_directory,accepted_extensions,path="injest"):
    
    total_files = []
    accepted_files = []
    
    for f in listdir(path):
        if isfile(join(path, f)):
            total_files.append(join(path, f))        
    
    for i in total_files:
        x = i.split(".")
        if x[1] in accepted_extensions:
            accepted_files.append(i)
        
    return accepted_files



def check_directory(parentdirectory,directory_name):
    if os.path.exists(os.path.join(parentdirectory,directory_name)):
        if os.path.isdir(os.path.join(parentdirectory,directory_name)):
            return True
        else:
            return False
    else:
        return False

def create_directory(parentdirectory,directory_name):
    try:
        os.mkdir(os.path.join(parentdirectory,directory_name))
    except FileExistsError:
        if os.path.isdir(os.path.join(parentdirectory,directory_name)):
            return True
        else:
            new_name = str(directory_name + '.bak')
            print(f'#. Renaming conflicting file name: {directory_name} to {new_name}')
            os.rename(os.path.join(parentdirectory,directory_name),os.path.join(parentdirectory,new_name))
            os.mkdir(os.path.join(parentdirectory,directory_name))
            return True
    return True
    
