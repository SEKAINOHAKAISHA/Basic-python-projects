import argparse
import sys


def calc(args):
    try:
        if(args.o == 'add'):
            return args.x+args.y
        elif(args.o == 'sub'):
            return args.x - args.y
        elif(args.o == 'mul'):
            return args.x * args.y
        elif(args.o == 'div'):
            return args.x / args.y
        else:
            return "Something went wrong"
    except:
        return "Exception Occured"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='This is the first argument')
    parser.add_argument('--y', type=float, default=3.0, 
                        help='This is the second argument')
    parser.add_argument('--o', type=str, default='add',
                         help='This is the operator')
    
    #parse_args function extracts data from command line and parses the data and assigns the data to attributes
    args = parser.parse_args()

    #this writes the result of calling calc function to the command line
    sys.stdout.write(str(calc(args)))
