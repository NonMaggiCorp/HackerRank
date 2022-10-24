#!/bin/python3

import os

def kangaroo(x1, v1, x2, v2):
    if x1 > x2:
        first_kangaroo = (x1, v1)
        last_kangaroo = (x2, v2)
    else:
        first_kangaroo = (x2, v2)
        last_kangaroo = (x1, v1)

    if  first_kangaroo[1] > last_kangaroo[1] :
        return("NO")
    else:
        for i in range(0,10000+1):
            if x1+(v1*i) == x2+(v2*i):
                return("YES")
        else:
            return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
