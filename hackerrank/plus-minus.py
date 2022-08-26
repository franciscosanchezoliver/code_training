#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    """
    Output Format:
        Print the following  lines, each to  decimals:

        proportion of positive values
        proportion of negative values
        proportion of zeros
    """
    positives, negatives, zeros = 0, 0, 0 
    for each_number in arr:
        if each_number < 0: negatives += 1
        elif each_number > 0: positives += 1
        else: zeros += 1

    print("%.6f" % (positives / len(arr)))
    print("%.6f" % (negatives / len(arr)))
    print("%.6f" % (zeros / len(arr)))
        

    # Write your code here
    print("hlla")

if __name__ == '__main__':
    n = [-4, 3, -9, 0, 4, 1] 

    plusMinus(n)
