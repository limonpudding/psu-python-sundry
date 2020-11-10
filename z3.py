import os
# E9 E8 7x

def find_codes(path):
    for entry in os.listdir(path):
        file = f"{path}\\{entry}"
        print(file)
        if os.path.isfile(file):
            with open(file, 'rb') as f:
                content = f.read()
            if content[0] == 233 or content[0] == 232 or (112 <= content[0] <= 127):
                print(file)


if __name__ == '__main__':
    path = "C:\\Users\\limonpudding\\Pictures\\"
    find_codes(path)
