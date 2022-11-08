import argparse

def function_1():
    print("hello world")

def function_2():
    print("hi world")

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--keywords', help='Climate Change Keywords to use for google search')
    parser.add_argument('--source', required=True)
    args=parser.parse_args()
    print(args.keywords)



