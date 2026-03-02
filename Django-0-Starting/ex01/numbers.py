def printNumbers():
    f = open("numbers.txt", "r")
    content = f.read()
    f.close
    
    numbers_list = content.split(',')
    for num in numbers_list:
        print (num)
    

if __name__ == '__main__':
    printNumbers()