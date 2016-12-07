flag = True
while(flag):
    try:
        file_name = input("Enter a filename: ")
        file_pointer = open(file_name)
        for each in file_pointer:
            print(each)
        file_pointer.close()
        flag = False
    except FileNotFoundError:
        print("Enter a valid filename.")