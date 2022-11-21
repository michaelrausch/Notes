"""
The argparse is used to get command line arguments when executing a script.

Example usages:

python arg_parser.py -h

python arg_parser.py -w 5 --height 10

python arg_parser.py --width 10 --height 10 -v

python arg_parser.py -w 10 -H 10 -q

python3.exe arg_parser.py -w 10 -H 10 -a cats -l dogs -a cats2
"""

import math
import argparse

"""
-w is the shorthand version
--width is the long version (required)

Without required=True, the argument will be defauted to `None`
"""
parser = argparse.ArgumentParser(description='Calculate area of the rectangle')
parser.add_argument('-w', '--width', 
                    type=int, 
                    required=True, 
                    help='Width of rectangle')
# -h is required for help, therefore -H is used..
parser.add_argument('-H', '--height', 
                    type=int, 
                    required=True, 
                    help='Height of rectangle')

"""
action=store_store automatically creates a default value of `False`

With mutually exclusive groups, only one can be specified at a time,
i.e. `python arg_parser.py -w 10 -H 10 -q -v` will throw an error.
"""
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='Print quietly')
group.add_argument('-v', '--verbose', action='store_true', help='Print verbose')

"""
To give an undetermined amount of parameters for a single variable you need
to utilize the `nargs` option or the `append` setting of the `action` option,
depending on how you want the user interface to behave.
"""
parser.add_argument(
    '-l', '--list',
    nargs='+', # '+' takes 1 or more arguments, '*' takes zero or more.
    help='Test variable that takes 1 or more values using nargs'
)

parser.add_argument(
    '-a', '--append',
    action='append', # '+' takes 1 or more arguments, '*' takes zero or more.
    help='Test variable that takes 1 or more values using nargs'
)

# With `append` you provide the option multiple times to build up the list.
# e.g. # python arg.py -a 1234 -a 2345 -a 3456 -a 4567
args = parser.parse_args()

def area_of_rectangle(width, height):
    return width * height

if __name__ == '__main__':
    area = area_of_rectangle(args.width, args.height)
    if args.quiet:
        print(area)
    elif args.verbose:
        print(f"The area of the rectangle with width: {args.width} and " \
        f"height: {args.height} is {area}")
    else:
        print(f"Area of rectangle = {area}")
        
    print("Values using -l", args.list)
    print("Values using -a", args.append)
    
