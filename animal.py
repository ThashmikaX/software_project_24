import sys

def dog():
    print("bow")

def default():
    print("hellow")

def main():
    default()

if __name__=='__main__':
    if sys.argv[1] == 'dog':
        dog()
    else:
        main()