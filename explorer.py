import pathlib

def choose_folder(folder: str) -> pathlib.Path | None:
    path_folder = pathlib.Path(folder)

    if not path_folder.exists():
        print("Folder does not exist!")
        return None
    
    if not path_folder.is_dir():
        print("This is not a folder!")
        return None
    
    return path_folder

def show_all(folder: Path):
    
    print("=============== ALL ITEMS ===============\n")

    for obj in folder.iterdir():
        print(f"📁 {obj.name}" if obj.is_dir() else f"📄 {obj.name}")
    
    print("\n=============== ALL ITEMS ===============")

def show_files(folder: Path):
    
    print("=============== ALL FILES ===============\n")

    for obj in folder.iterdir():
        if obj.is_file():
            print(f"📄 {obj.name}")
    
    print("\n=============== ALL FILES ===============")

def show_folders(folder: Path):
    
    print("=============== ALL FOLDERS ===============\n")

    for obj in folder.iterdir():
        if obj.is_dir():
            print(f"📁 {obj.name}")
    
    print("\n=============== ALL FOLDERS ===============")

def count_files(folder: Path):

    print("=============== FILE COUNT ===============\n")

    print(f"📄 Total files: {len(list(item for item in folder.iterdir() if item.is_file()))}")

    print("\n=============== FILE COUNT ===============")

def count_folders(folder: Path):

    print("=============== FOLDER COUNT ===============\n")

    print(f"📁 Total folders: {len(list(item for item in folder.iterdir() if item.is_dir()))}")

    print("\n=============== FOLDER COUNT ===============")

def show_file_information(folder: Path, filename: str):
    if not filename.strip():
        print("File name cannot be empty.")
        return False
    
    file_path = folder / filename

    if not file_path.exists():
        print("File does not exist!")
        return False
    if file_path.is_dir():
        print("This is not a file!")
        return False
    
    print(f'''
    =============== FILE INFORMATION ===============

    📄 Name   : {file_path.name}
    📝 Stem   : {file_path.stem}
    🏷️  Suffix : {file_path.suffix}
    📂 Parent : {file_path.parent}

    ===============================================
    ''')

    return True

def extension_statistics(folder: Path):
    dic = {}

    for item in folder.iterdir():
        if item.is_dir():
            continue

        suffix = item.suffix if item.suffix else "<No Extension>"

        if suffix not in dic:
            dic[suffix] = 1
        else:
            dic[suffix] += 1
        
    print("=============== EXTENSION STATISTICS ===============\n")

    print("\n".join(f"📄 {suffix: <18}: {count} files" for suffix, count in dic.items()))

    print("\n=============== EXTENSION STATISTICS ===============\n")


def folder_summary(folder: Path):
    print(f'''
    ================ FOLDER SUMMARY ================

    📂 Folder Name     : {folder.name}
    📁 Total Folders   : {len(list(item for item in folder.iterdir() if item.is_dir()))}
    📄 Total Files     : {len(list(item for item in folder.iterdir() if item.is_file()))}
    📦 Total Items     : {len(list(item for item in folder.iterdir()))}

    ===============================================
    ''')

def pause():
    input("\nPress enter to continue...")



