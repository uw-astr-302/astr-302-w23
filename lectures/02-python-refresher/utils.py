""" A module with useful functions """
import sys, re

def exit_with_usage():
    """ Prints a usage message and exits the program. """
    print("")
    print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
    exit(0)

def number_or_exit(s, msg):
    """ Test if argument s is a number, abort execution otherwise. """
    isNumber = r'^[1-9][0-9]*\.?[0-9]*([Ee][+-]?[0-9]+)?$';

    if not re.search(isNumber, s):
        print("Error: the {} argument must be a number".format(msg))
        exit_with_usage()

