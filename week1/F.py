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
     
    # sys.stdout.write(str('yes') + "\n")
     
############ ---- Problem Solution ---- ############
def main():
    n = float(input().split()[0])
    s = insr()
    s2 = insr().split()[0]
    sys.stdout.write(f"{s}: {round(n, 3):.3f} \n{s2}")
     
if __name__ == '__main__':
    main()