# -*- coding: utf-8 -*-
"""
Created on   Fri Apr 27 08:04:29 2018
Completed on Fri Apr 27 16:58:05 2018

@author: Karan
"""
def summing(a, b):
    a = str(a)
    b = str(b)
    if (len(a) < len(b)):
#        swap(a, b)
        temp = a
        a = b
        b = temp
    alen = len(a)
    blen = len(b)
#    now a has more digits than b
    ans = ""
    carry = 0
# reversing a and b
    a = a[::-1]
    b = b[::-1]
    for i in range(blen):
        middle = str(int(a[i]) + int(b[i]) + carry)
        if (len(middle) == 1):
            ans += middle[0]
            carry = 0
        elif (len(middle) == 2):
            ans += middle[1]
            carry = int(middle[0])
        else:
            print('error in summing')

    if (carry == 0 and alen > blen):
        for i in range(blen, alen):
            ans += a[i]
    elif (alen == blen and carry != 0):
        ans += str(carry)
        carry = 0
    elif (alen > blen and carry != 0):
        i = 0
        while (carry != 0):
            if (blen + i > alen - 1):
                ans += str(carry)
                carry = 0
            else:
                another = str(int(a[blen + i]) + carry)
                if (len(another) == 1):
                    ans += another[0]
                    carry = 0
                elif (len(another) == 2):
                    ans += another[1]
                    carry = int(another[0])
                else:
                    print('error in summing in final carry')
                i += 1
        for j in range(blen + i, alen):
            ans += a[j]

    ans = ans[::-1]
    return ans

def multiply(a, b):
    a = str(a)
    b = str(b)
    alen = len(a)
    blen = len(b)
    solution = []
    carry = 0
#   middle --> 2 digit and carry --> 1 digit
    for j in range(blen):
        part = ""
        for i in range(alen):
            middle = str(int(a[alen - 1 - i]) * int(b[blen - 1 - j]) + carry)
            if (len(middle) == 1):
                part += middle[0]
                carry = 0
            elif (len(middle) == 2):
                part += middle[1]
                carry = int(middle[0])
            else:
                print('error in multiply')
        if (carry != 0):
            part += str(carry)
            carry = 0
        part = part[::-1]
        solution.append(part)

    total = "0"
    for i in range(len(solution)):
        zeros = ''
        for j in range(i):
            zeros += '0'
#        print(solution[i] + zeros)
        total = summing(total, solution[i] + zeros)
    return total

def extraLongFactorials(n):
    # Complete this function
    if (n <= 1):
#        print(1)
        return 1
    else:
        product = str(1)
        for i in range(2, int(n + 1)):
#           now multiply product by the next number, i, but both are strings
            product = multiply(product, str(i))
#            print(i, product)
        print(product)
        return product

if __name__ == "__main__":
    n = int(input().strip())
    y = extraLongFactorials(n)