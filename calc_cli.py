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
    except Exception as error:
        #returns exception name as well
        return f'An error occurred: {type(error).__name__}'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n1', type=float, default=1.0,
                        help='This is the first number')
    parser.add_argument('n2', type=float, default=3.0, 
                        help='This is the second argument')
    parser.add_argument('ops', type=str, default='add',
                         help='This is the operation to be done')
    
    #parse_args function extracts data from command line and parses the data and assigns the data to attributes
    args = parser.parse_args()

    #this writes the result of calling calc function to the command line
    sys.stdout.write(str(calc(args)))
