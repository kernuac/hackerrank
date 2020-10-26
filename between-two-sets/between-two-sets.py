#!/bin/python3

import math
import os
import random
import re
import sys

def get_total_x( arr, brr ):
    print(arr)
    print(brr)
    arr_result = []
    result = 0
    for b in brr :
        arr_result += get_factors( b )
    arr_result = list( dict.fromkeys( arr_result ) )

    print(arr_result)
    
    for f in arr_result:
        cnt = 0
        for i in arr:
            if f % i == 0:
                cnt = cnt + 1
        if len(arr) == 1 and len( arr_result ) == cnt:
            return 1
         
        if cnt == len(arr):
            result = result + 1
    
    return result

def get_factors( element ):
    return [ x for x in range( 1, element + 1) if element % x == 0 ]

def get_gcd( number ):
    

if __name__ == '__main__':
    #fptr = open( os.environ['OUTPUT_PATH'], 'w' )
    first_multiple_input = input().rstrip().split()
    n = int( first_multiple_input[0] )
    m = int( first_multiple_input[1] )
    arr = list( map ( int, input().rstrip().split() ) )
    brr = list( map ( int, input().rstrip().split() ) )
    total = get_total_x( arr, brr )
    print(total)
    #fptr.write( str( total ) + '\n' )
    #fptr.close()
