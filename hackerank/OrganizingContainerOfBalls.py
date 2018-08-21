#!/bin/python3
# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.


def organizingContainers(container):
    numberInEachContainer = list(map(lambda x: sum(x), container))
    numberOfEachGroup = []
    for i in range(len(container[0])):
        count = 0
        for j in range(len(container)):
            count += container[j][i]
        numberOfEachGroup.append(count)
    numberInEachContainer.sort()
    numberOfEachGroup.sort()
    return "Possible" if numberInEachContainer == numberOfEachGroup else "Impossible"
