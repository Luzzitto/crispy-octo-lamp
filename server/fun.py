import os

def get_files(folder_path, exclude=["Volume System Information"]):
    file_list = []
    for dirs, subdirs, files in os.walk(folder_path):
        subdirs[:] = [d for d in subdirs if d not in exclude]
        for file in files:
            file_list.append(os.path.join(dirs, file))
    return file_list
