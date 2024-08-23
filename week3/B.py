# Template Codeforces
import sys
import math as m
input = sys.stdin.readline
     
    ############ ---- Input Functions ---- ############
def inp(): #integer
    return(int(input()))
def inlt(): # list
    return(list(map(int,input().split())))
def insr(): # string
    s = input()
    return("".join(list(s[:len(s) - 1])))
def invr(): # separated int
    return(map(int,input().split()))
     
    # sys.stdout.write(str('yes') + "\n")
     
############ ---- Problem Solution ---- ############
def main():
    a, op, b = input().split()
    if op == "+":
        sys.stdout.write(str(int(a) + int(b)))
    elif op == "-":
        sys.stdout.write(str(int(a) - int(b)))
    elif op == "*":
        sys.stdout.write(str(int(a) * int(b)))
    elif op == "/":
        if int(b) == 0:
            sys.stdout.write("ERROR")
        else:
            sys.stdout.write(f"{round(int(a) / int(b), 2):.2f}")
     
if __name__ == '__main__':
    main()