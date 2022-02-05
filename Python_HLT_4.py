def main():
    #Maximum multiple
    multiplyMax = 12
    #Current multiple
    multiple = 1
    #Obtain number to multiple with
    number = int(input("Give me a number: "))

    while multiple <= multiplyMax:
        print(number, "x", multiple, "=", number*multiple)
        multiple = multiple + 1

main()