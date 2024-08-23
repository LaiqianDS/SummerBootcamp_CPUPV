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
    weather = insr()
    temp = inp()
    people = []
    people.append("Adrian") if weather == "Soleado" and temp >= 20 else None
    people.append("Barbara") if weather == "Soleado" or temp > 15 else None
    people.append("Carmen") if weather == "Soleado" or weather == "Nublado" else None
    people.append("Dario") if weather != "Tormenta" else None
    sys.stdout.write("Vienen a pasear: "+ " ".join(people))
     
if __name__ == '__main__':
    main()