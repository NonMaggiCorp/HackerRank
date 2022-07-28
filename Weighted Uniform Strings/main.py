#!/bin/python3

import os

def weightedUniformStrings(s, queries):
    splited_string=split_string(s)
    print(splited_string)
    set_a=calculate_weight(splited_string)
    list_a=[]
    for i in queries:
        if i in set_a:
            list_a.append("Yes")
        else:
            list_a.append("No")
    return(list_a)

def split_string(string):
    split_string=set()
    length=0
    for i in range(0,len(string)):
        if i == len(string)-1:
            if string[i]==string[i-1]:
                length+=1
                continious_string=string[i-1]*length
                split_string.add(continious_string)
            else:
                split_string.add(string[i])
        if i == 0:
            length+=1
        elif string[i]==string[i-1]:
            length+=1
        else:
            continious_string=string[i-1]*length
            split_string.add(continious_string)
            length=1
    return(split_string)

def calculate_weight(splitted_string):
    set_a=set()
    for i in splitted_string:
        for j in range(1,len(i)+1):
            value=(ord(i[0])-96)*j
            set_a.add(value)
    return(set_a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
