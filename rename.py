import os

def remove_spaces(name):
    """ Delete all the SPACE in the name """
    while " " in name:
        name = name.replace(" ", "")
    return name

def rename_files_in_folder(folder_path):
    count = 1

    # run of all file in the folder
    for entry in os.listdir(folder_path):
        entry_path = os.path.join(folder_path, entry)

        if os.path.isdir(entry_path):  # if we find a folder
            cleaned_folder_name = remove_spaces(entry)  # delet the SPACE in the name of file
            new_folder_path = os.path.join(os.path.dirname(entry_path), cleaned_folder_name)
            if new_folder_path != entry_path:  # if the new name is not same as the old name, then rename the folder
                os.rename(entry_path, new_folder_path)
                print(f'Renamed folder: "{entry_path}" to "{new_folder_path}"')
            
            rename_files_in_folder(new_folder_path)
        elif os.path.isfile(entry_path):  # if we find a file
            # protect the python file
            if entry.endswith(".py"):
                continue
            
            # get the name of the folder which conclude the file
            folder_name = remove_spaces(os.path.basename(folder_path))
            # create the new file name
            cleaned_entry_name = remove_spaces(entry)  # delete the SPACE
            new_file_name = f'{folder_name}({count}){os.path.splitext(cleaned_entry_name)[1]}'
            new_file_path = os.path.join(folder_path, new_file_name)
            # rename the file
            os.rename(entry_path, new_file_path)
            print(f'Renamed file: "{entry}" to "{new_file_name}"')
            count += 1  # a count for the name of the file

# setting for the path of the first folder (the example is the folder of this file.py)
initial_folder = os.path.dirname(os.path.abspath(__file__))
rename_files_in_folder(initial_folder)

print('HAVE RENAMED ALL THE FILES')
