#!/bin/python3

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count=0
    for i in apples:
        apple_position=a+i
        if apple_position >= s and apple_position <= t:
            count+=1
    print(count)
    count=0
    for j in oranges:
        orange_position=b+j
        if orange_position <= t and orange_position >= s:
            count+=1
    print(count)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)