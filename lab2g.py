#!/usr/bin/env python3

# Author: Bassil Akar
# Author ID: bakar
# Date Created: 2024/12/8

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
