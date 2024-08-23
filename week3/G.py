# Template Codeforces
import sys
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
          
############ ---- Problem Solution ---- ############
def main():
    for i in range(1, inp()+1):
        if i%3 == 0 and i%5 == 0:
            sys.stdout.write("FizzBuzz\n")
        elif i%3 == 0:
            sys.stdout.write("Fizz\n")
        elif i%5 == 0:
            sys.stdout.write("Buzz\n")
        else:
            sys.stdout.write(str(i)+"\n")
        
if __name__ == '__main__':
    main()