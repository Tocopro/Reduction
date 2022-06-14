
from math import gcd


def reduction():
    numerate, denominate = input_user()
    remainder = gcd(numerate, denominate)
    numerate = numerate // remainder
    denominate = denominate // remainder
    print("The Smallest fraction of the  fraction ", numerate, "/", denominate)


def input_user():
    numerator = int(input("Enter the Numerator: "))
    denominator = int(input("Enter the Denominator: "))
    if numerator > denominator:
        print("The Numerator can not be greater than denominator: ")
        input_user()
    else:
        return numerator, denominator


reduction()
