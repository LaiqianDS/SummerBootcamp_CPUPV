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
    line = insr().strip()
    while len(line):
        if len(line) % 2 == 1:
            sys.stdout.write(line)
        else: 
            sys.stdout.write(line[::-1])
        sys.stdout.write('\n')  
        line = insr().strip()          
        
if __name__ == '__main__':
    main()