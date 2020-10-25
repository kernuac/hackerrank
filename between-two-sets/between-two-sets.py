#!/bin/python3

import math
import os
import random
import re
import sys

def get_total_x( a, b ):
    pass

if __name__ == '__main__':
    fptr = open( os.environ['OUTPUT_PATH'], 'w' )
    first_multiple_input = input().rstrip().split()
    n = int( first_multiple_input[0] )
    m = int( first_multiple_input[1] )
    arr = list( map ( int, input().rstrip().split() ) )
    brr = list( map ( int, input().rstrip().split() ) )
    total = get_total_x( arr, brr )
    fptr.write( str( total ) + '\n' )
    fptr.close()
