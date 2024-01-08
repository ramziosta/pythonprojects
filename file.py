counter = 0
total = 0.0
smallest = None
largest = None

while True:
    stringVal = input("Enter a number: ")
    if stringVal == "done":
        break
    try:
        fVal = float(stringVal)
        if smallest is None or fVal < smallest:
            smallest = fVal
        if largest is None or fVal > largest:
            largest = fVal
    except ValueError:
        print("Invalid input, Please enter a number.")
        continue

    print("The number you entered is: ", fVal)
    counter += 1
    total += fVal
    print("Current counter: ", counter)
    print("Current total: ", total)
    print("Current largest number is: ", largest)
    print("Current smallest number is: ", smallest)
    print("-----------------------------------")

print("All Done!!!")
print("Final Counter: ", counter)
print("Final Total: ", total)
print("The largest number is: ", largest)
print("The smallest number is: ", smallest)

found = False
numArray = [34, 5, 1, 24, 6, 7, 9, 43, 3, 88, 65]
print("hello", found)
for number in numArray:
    print(number)
    if number == 3:
        found = True
        print("I found the number: ", found, number)
        break
print('World!')
# TODO write more code
