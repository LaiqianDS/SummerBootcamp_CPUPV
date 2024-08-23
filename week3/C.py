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
    PI = 3.141592
    for _ in range(inp()):
        nums = input().split()
        if int(nums[0]) == 1:
            sys.stdout.write(f"{(PI*float(nums[1])**2):.6f}\n")
        elif int(nums[0]) == 2:
            sys.stdout.write(f"{(float(nums[1])**2):.6f}\n")
        elif int(nums[0]) == 3:
            sys.stdout.write(f"{(float(nums[1])*float(nums[2])):.6f}\n")
        else:
            sys.stdout.write(f"{((float(nums[1])*float(nums[2]))/2):.6f}\n")
        
if __name__ == '__main__':
    main()