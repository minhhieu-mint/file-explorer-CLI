from explorer import (
    choose_folder,
    show_all,
    show_files,
    show_folders,
    count_files,
    count_folders,
    show_file_information,
    extension_statistics,
    folder_summary,
    pause
)

current_folder = None

while True:
    print(f'''
    ================= FILE EXPLORER =================

    Current folder: {current_folder if current_folder else 'Not Selected'}

    1. Select Folder

    2. Show All Items
    3. Show Only Files
    4. Show Only Folders

    5. Count Files
    6. Count Folders

    7. Show File Information
    8. Extension Statistics
    9. Folder Summary

    10. Exit

    =================================================
    ''')
    choice = input("Enter a number (1-10): ")

    if not choice.isdigit():
        print("Please enter a number!")
        continue
    if not (1 <= int(choice) <= 10):
        print("Please enter a number between 1-10!")
        continue

    if choice == "1":
        while True:
            new_folder = input("Enter new folder: ")

            current_folder = choose_folder(new_folder)

            if current_folder:
                break
        continue

    if current_folder is None:
        print("Please select a folder first!")
        continue
    
    if choice == "2":
        show_all(current_folder)
        pause()
    elif choice == "3":
        show_files(current_folder)
        pause()
    elif choice == "4":
        show_folders(current_folder)
        pause()
    elif choice == "5":
        count_files(current_folder)
        pause()
    elif choice == "6":
        count_folders(current_folder)
        pause()
    elif choice == "7":
        while True:
            filename = input("Enter a file: ")

            if show_file_information(current_folder, filename):
                pause()
                break
    elif choice == "8":
        extension_statistics(current_folder)
        pause()
    elif choice == "9":
        folder_summary(current_folder)
        pause()
    elif choice == "10":
        break
    else:
        print("Error!")

print("Program exited.")

