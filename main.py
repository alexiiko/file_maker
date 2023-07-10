import os
from file_extensions import file_extensions

def create_file(file_name, file_extension, file_path):
    file_path = os.path.join(file_path, file_name+file_extension)
    file_path_name = os.path.dirname(file_path)

    file_data = open(file_path, "w")
    file_data.close()

    print(f"Succesfully created {file_name}{file_extension} in {file_path_name}.")

def create_folder(folder_name, folder_path):
    folder_path = os.path.join(folder_path, folder_name)
    folder_path_name = os.path.dirname(folder_path)

    os.makedirs(folder_path)

    print(f"Succesfully created {folder_name} in {folder_path_name}.")

file_folder = input("Do you want to create a file or folder? ").lower()
print()
while True:
    if file_folder == "file":
        file_extension = input("Choose file extension: " + " | ".join(file_extensions) + " :").lower()
        file_name = input("Enter the file name: ")
        file_path = input("Enter the path of the file: ")

        if file_extension not in file_extensions:
            print("This file extension is not supported.")
            continue
        for extension in file_extensions:
            if file_extension == extension:
                create_file(file_name, file_extension, file_path)
                break

        print()
        make_another_file_or_folder = input("Do you want to create another file or folder? Y/N ").upper()

        if make_another_file_or_folder == "Y":
            file_folder = input("Do you want to create a file or folder? ").lower()
            print()
            continue
        elif make_another_file_or_folder == "N":
            break
        else:
            print("Wrong input.")
            make_another_file_or_folder = input("Do you want to create another file or folder? Y/N ").upper()
            continue
    elif file_folder == "folder":
        folder_path = input("Enter the path of the folder: ")
        folder_name = input("Enter the name of the folder: ")
        create_folder(folder_name, folder_path)
        print()

        make_another_file_or_folder = input("Do you want to create another file or folder? Y/N ").upper()
        if make_another_file_or_folder == "Y":
            file_folder = input("Do you want to create a file or folder? ").lower()
            print()
            continue
        elif make_another_file_or_folder == "N":
            break
        else:
            print("Wrong input.")
            make_another_file_or_folder = input("Do you want to create another file or folder? Y/N ").upper()
            continue

    else:
        print("Wrong input.")
        file_folder = input("Do you want to create a file or folder? ").lower()
        print()
        continue