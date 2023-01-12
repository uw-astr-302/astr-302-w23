#!/usr/bin/env python

import sys
import re
import utils

#### The main program begins here

if len(sys.argv) != 3:
    print("Error: two arguments required.")
    utils.exit_with_usage()

utils.number_or_exit(sys.argv[1], 'first')
utils.number_or_exit(sys.argv[2], 'second')

a = float(sys.argv[1])
b = float(sys.argv[2])

print (a + b)
