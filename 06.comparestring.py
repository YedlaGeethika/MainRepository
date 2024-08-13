def stringcompare(inputstring):
    inputstring = inputstring.lower()
    e = inputstring.count('e')
    a = inputstring.count('a')

    return e == a


while True:
    inputstring = input("Enter a string (or type 'exit' to quit): ")

    if inputstring.lower() == 'exit':
        break

    result = stringcompare(inputstring)
    print(f"The result for the string '{inputstring}' is: {result}")

