
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


print(sumOfList([1, 2, 3]))
print(productOfList([1, 2, 3, 4]))