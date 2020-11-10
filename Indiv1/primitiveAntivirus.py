import os


def hasSignature(filePath, sign):
    targetFile = open(filePath, 'rb')
    bytes = targetFile.read()
    sign_length = len(sign)
    for start in range(len(bytes) - sign_length):
        if bytes[start:sign_length] == sign:
            return True
    return False


def defineSignature(dirPath, virusPath):
    virus = open(f"{virusPath}", 'rb')
    found = False
    for sign_length in range(32, 257):
        # для всех возможных длин сигнатуры от 32 до 256 байт смотрим, есть ли такая сигнатура в других файлах
        bytes = virus.read()
        for start in range(len(bytes) - sign_length):
            sign = bytes[start:start+sign_length]
            for entry in os.listdir(dirPath):
                found = hasSignature(f"{dirPath}\\{entry}", sign)
                if found:
                    break
            if found:
                break
            else:
                print("Найдена уникальная сигнатура")
                return sign
        if found:
            print(f"Для длины {sign_length} нет уникальной сигнатуры!")


def findVirus(dirPath, sign):
    for entry in os.listdir(dirPath):
        found = hasSignature(f"{dirPath}\\{entry}", sign)
        if found:
            print(f"Найден вирус: {entry}")


virusPath = 'COFFSHOP.COM'
sign = defineSignature("forSignIdentify", virusPath)
findVirus("withVirus", sign)











