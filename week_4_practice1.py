def main():
    name = input("Enter your name: ")
    name = name.upper()
    #vowels = "aeiouAEIOU"
    
    count = 0

    for each in name:
        if each in vowels:
            count += 1

    print("Out of {} letters, {} has {} vowels".format(len(name), name, count))
main()