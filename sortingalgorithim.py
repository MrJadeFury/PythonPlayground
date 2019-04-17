import array as arr

numberone = input("Enter 1st # ")
try:
    val = int(numberone)
    print("# is an int")
    print("Value = " + numberone)
    numberone = val
except ValueError:
    print("Error not an int")
numbertwo = input("Enter 2nd # ")
try:
    val = int(numbertwo)
    print("# is an int")
    print("Value = " + numbertwo)
    numbertwo = val
except ValueError:
    print("Error not an int")
numberthree = input("Enter 3rd # ")
try:
    val = int(numberthree)
    print("# is an int")
    print("Value = " + numberthree)
    numberthree = val
except ValueError:
    print("Error not an int")
numberfour = input("Enter 4th # ")
try:
    val = int(numberfour)
    print("# is an int")
    print("Value = " + numberfour)
    numberfour = val
except ValueError:
    print("Error not an int")
numberfive = input("Enter 5th # ")
try:
    val = int(numberfive)
    print("# is an int")
    print("Value = " + numberfive)
    numberfive = val
except ValueError:
    print("Error not an int")
numbersix = input("Enter 6th # ")
try:
    val = int(numbersix)
    print("# is an int")
    print("Value = " + numbersix)
    numbersix = val
except ValueError:
    print("Error not an int")
numberseven = input("Enter 7th # ")
try:
    val = int(numberseven)
    print("# is an int")
    print("Value = " + numberseven)
    numberseven = val
except ValueError:
    print("Error not an int")
intarray = arr.array('i', [numberone, numbertwo, numberthree, numberfour, numberfive, numbersix, numberseven])
print("Current Array: ")
for i in intarray:
    print(i, end=" ")
print("Sorting Array")
def insertion_sort(arr, simulation=False):
    for i in range(len(intarray)):
        cursor = intarray[i]
        pos = i

        while pos > 0 and intarray[pos-1] > cursor:
            intarray[pos] = intarray[pos-1]
            pos = pos-1
        intarray[pos] = cursor
    print ("Sorted Array: " + intarray)