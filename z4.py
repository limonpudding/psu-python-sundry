import os

# есть MZ но нет PE00 в смещении 0400h

def find_mz(path):
    for entry in os.listdir(path):
        file = f"{path}\\{entry}"
        if os.path.isfile(file):
            with open(file, 'rb') as f:
                content = f.read()
                found = content[0:2] == b'MZ' and content[1024:1028] != b'PE\x00\x00'
                if found:
                    print("MZ file without PE00: "+file)


if __name__ == '__main__':
    path = "C:\\Users\\limonpudding\\Documents\\PSU\\Защита от вирусов\\DOSBOX\\WORK"
    find_mz(path)
