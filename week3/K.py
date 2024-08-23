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
    T = inp()
    for _ in range(T):
        N, C = invr()
        bombones = inlt()
        if C in bombones:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
        
        
if __name__ == '__main__':
    main()