import os

# folder path
dir_path = r'/home/alex/Documents/work_files/workspace/python/home work/Python_homeworks/crate_folders_types/files'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)