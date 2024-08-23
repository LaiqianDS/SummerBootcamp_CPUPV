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
    nums = inlt()
    ans = []
    for num in nums:
        ans.append(num+ans[-1] if ans else num)
    sys.stdout.write(" ".join([str(x) for x in ans]))
        
if __name__ == '__main__':
    main()