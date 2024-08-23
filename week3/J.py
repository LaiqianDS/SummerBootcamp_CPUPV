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
    last = line
    while len(line):
        last = line
        line = insr().strip()
        
    sys.stdout.write(last)
    
        
        
if __name__ == '__main__':
    main()