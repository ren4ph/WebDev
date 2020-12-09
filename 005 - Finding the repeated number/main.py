import random as rd


def repeats(numbers):
    '''Finds Repeat Numbers'''
    temp = [0] * len(numbers)
    tem = []
    for number in numbers:
        temp[number] += 1
    for i in range(len(temp)):
        if temp[i] > 1:
            tem.append(i)
    return (set(tem), temp)


while True:
    numbers = [rd.randrange(1, 4000) for i in range(100) if True]
    numbers.sort()
    print(numbers)
    if len(set(numbers)) < len(numbers):
        print("There are repeats!")
        repeat, which = repeats(numbers)
    else:
        print("There are no repeats!")
    x = input("Press any key to show how many, or press enter to continue:")
    if x:
        print(which)
    x = input("Press any key to stop, or press enter to continue:")
    if x:
        break
    input("Press enter to continue")
