def main():
    x = input("Input a list of number (Seperate with spaces)")
    arr = [float(i) for i in x.split()]
    
    print("Sum of array: ", sumOfList(arr))
    print("Product of array: ", productOfList(arr))
    print("Reversed array: ", reverseList(arr))

def sumOfList(input):
    size = 0
    for i in input:
        size += i
    return size

def productOfList(input):
    size = 1
    for i in input:
        size *= i
    return size

def reverseList(input):
    input.reverse()
    return input
