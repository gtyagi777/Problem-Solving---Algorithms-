# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:33:51 2019

@author: tyagi
"""

#!/bin/python3

import math
import os
from collections import defaultdict

# Complete the sockMerchant function below.
def sockMerchant(n, arr):
    dict_ = defaultdict(int)
    for i in arr:
        dict_[i] += 1

    count_ = 0

    for key,value in dict_.items():
        count_ += math.floor(value/2)

    return count_


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()