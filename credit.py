from cs50 import get_string


def main():
    cc = get_string("Number: ")
    cclength = len(cc)
    amex = validAMEX(cc, cclength)
    mc = validMasterCard(cc, cclength)
    visa = validVisa(cc, cclength)

    if checksum(cc) == False:
        print("INVALID")
    elif amex == True:
        print("AMEX")
    elif mc == True:
        print("MASTERCARD")
    elif visa == True:
        print("VISA")
    else:
        print("INVALID")


def checksum(cc):
    multbytwo = 0
    notmultbytwo = 0
    mult_two_array = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    for i in range(len(cc)):
        current = int(cc[len(cc) - 1 - i])
        if i % 2 == 0:
            notmultbytwo += current
        else:
            multbytwo += mult_two_array[current]
    total_sum = notmultbytwo + multbytwo
    return ((total_sum % 10) == 0)


def validAMEX(cc, cclength):
    first_two = int(cc[:2])
    if cclength == 15 and first_two == 37:
        return True
    elif cclength == 15 and first_two == 34:
        return True
    else:
        return False


def validMasterCard(cc, cclength):
    first_two_mc = int(cc) / 10**14
    if cclength == 16 and (50 < first_two_mc < 56):
        return True
    else:
        return False


def validVisa(cc, cclength):
    if cclength == 13:
        first_digit = int(cc[0])
        if first_digit == 4:
            return True
        else:
            return False
    elif cclength == 16:
        first_digit = int(cc[0])
        if first_digit == 4:
            return True
        else:
            return False
    else:
        return False


main()
