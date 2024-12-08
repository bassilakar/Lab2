#!/usr/bin/env python3

# Author: Bassil Akar
# Author ID: bakar
# Date Created: 2024/12/8

import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} timer_value")
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
