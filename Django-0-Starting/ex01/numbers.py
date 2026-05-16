def printNumbers():
    with open("numbers.txt", "r") as f:
        content = f.read().strip()
    numbers_list = content.split(',')
    for num in numbers_list:
        print(num)

if __name__ == '__main__':
    printNumbers()