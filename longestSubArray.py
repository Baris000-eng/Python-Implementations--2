#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def customSwapFunc(x,y):
    temp=x
    x=y
    y=temp
    
def absVal(t):
    if t<0:
        t=-t
    return t

#Selection sort algorithm in python
def customSort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i!=j and arr[i]<=arr[j]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
    return arr

    
def customMax(a,b):
    maxNum=a
    if b>=maxNum:
        maxNum=b
    return maxNum
                


#Description:
#My solution to the function finding the length of the #longest subarray of a such that the difference any 2 elements
#of a is less than or equal to 1

  
def pickingNumbers(a):
    customSort(a) #sorting numbers
    result=0
    currentArrLen=0
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if absVal(a[j] - a[i]) <= 1 and i!=j: #1,1,2,2,4,4,5,5,5
                currentArrLen=j-i+1
                result=customMax(result,currentArrLen)
    return result

    
            
    
   
                
        
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
