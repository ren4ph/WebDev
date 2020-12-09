print("Disclaimer: This will not work if a has a coeficcient or either number is negative.")
num = input("What is the number you want the factors of?: ")
num2 = input("What is the number you want?: ")

def print_factors(x):
    factors = []
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

def format_factors(x):
    if 1 or 3 or 5 or 7 or 9 in x:
        pairs = [[] * 2] * int((len(x) + 1) / 2)
    else:
        pairs = [[] * 2] * (len(x) / 2)
    if not len(x) >= 1:
        for i in pairs:
            pairs[i] = [x.pop(0), x.pop()]
    else:
        for i in range(int((len(x) - 1) / 2)):
            pairs[i] = [x.pop(0), x.pop()]
        temp = x.pop()
        pairs[len(pairs) - 1] = [temp, temp]
    return pairs

def pair_match(pairs, x):
    cool = []
    good = False
    for pair in pairs:
        if pair[0] + pair[1] == x:
            good = True
            cool.append(pair)
    if not good:
        print("Nothing good has appeared.")
    else:
        return cool

factors = print_factors(int(num))
print(factors)
pairs = format_factors(factors)
print(pairs)
matching_pairs = pair_match(pairs, int(num2))
print(matching_pairs)
