import argparse

def function_1():
    print("hello world")

def function_2():
    print("hi world")

if __name__ == '__main__':
    # function_1()
    # function_2()
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyword", help="Documentation about the parameter")
    parser.add_argument("--source", required=True)
    args=parser.parse_args()
    print(args.keyword)
