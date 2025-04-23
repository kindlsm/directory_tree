import os

def list_directory_contents(startpath, level=0, prefix=''):
    try:
        items = os.listdir(startpath)
        for i, item in enumerate(items):
            itempath = os.path.join(startpath, item)
            if i == len(items) - 1:
                connector = '└── '
                new_prefix = prefix + '    '
            else:
                connector = '├── '
                new_prefix = prefix + '│   '
            
            print(prefix + connector + item)
            if os.path.isdir(itempath):
                list_directory_contents(itempath, level + 1, new_prefix)
    except Exception:
        pass

def find_directory(root, target_path):
    for dirpath, dirnames, filenames in os.walk(root):
        if target_path.lower() in dirpath.lower():
            return dirpath
    return None

def main():
    dir_path = input("트리를 출력할 경로를 입력 : ").strip()
    target_dir = os.path.normpath(dir_path).lower()

    drives = [f"{chr(d)}:\\" for d in range(ord('A'), ord('Z') + 1) if os.path.exists(f"{chr(d)}:\\")]
    
    target_directory = None
    for drive in drives:
        target_directory = find_directory(drive, target_dir)
        if target_directory:
            break

    if target_directory:
        print(f"\n{target_directory}/")
        list_directory_contents(target_directory)


if __name__ == "__main__":
    main()
