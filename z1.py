import os


def print_files_2lvl(path):
    for entry in os.listdir(path):
        print(entry)
        if os.path.isdir(f"{path}\\{entry}"):
            for entry2lvl in os.listdir(f"{path}\\{entry}"):
                print(f"    {entry2lvl}")


if __name__ == '__main__':
    path = "C:\\Users\\limonpudding\\Pictures"
    print_files_2lvl(path)

