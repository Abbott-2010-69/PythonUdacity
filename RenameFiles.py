import os
def rename_files():
    #enter file path here
    file_list = os.listdir(r"C:\dest")
    saved_path = os.getcwd
    os.chdir(r"C:\dest")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()