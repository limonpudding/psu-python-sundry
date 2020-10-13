def find_sub_str(path, sub_str):
    file = open(path)
    counter = 1
    count_sub_str = 0
    for line in file:
        if line.find(sub_str) > -1:
            count_sub_str += 1
        counter +=1
    print(f"В {count_sub_str} абзацах есть искомая строка!")


if __name__ == '__main__':
    path = "C:\\Users\\limonpudding\\Pictures\\texts.txt"
    sub_str = "hey"
    find_sub_str(path, sub_str)

