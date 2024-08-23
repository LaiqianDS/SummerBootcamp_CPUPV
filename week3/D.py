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
    N, _ = invr()
    N = int(N)
    ans = []
    for num in invr():
        if N == int(num):
            ans.append("1p")
        elif abs(N-num) <= 5:
            ans.append("0.5p")
        elif abs(N-num) <= 10:
            ans.append("0.25p")
        else: ans.append("0p")
    sys.stdout.write(" ".join(ans))

        
if __name__ == '__main__':
    main()