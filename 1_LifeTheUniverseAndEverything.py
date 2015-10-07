# Repeat indefinitely until you read the number 42.
while True:
    inputNumber = int(raw_input())

    if inputNumber == 42:
        break
    else:
        print inputNumber

exit(0)