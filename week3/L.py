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
    P, V = invr()
    ans = 0
    for _ in range(P):
        windows = input().split()
        for pair in zip(windows[::2], windows[1::2]):
            if "#" in pair:
                ans += 1
    sys.stdout.write(str(ans))
        
        
if __name__ == '__main__':
    main()