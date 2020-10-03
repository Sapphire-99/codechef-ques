
def majorityElement(A,N):
    res=0
    n=len(A)
    co=1
    for i in range(1,n):
        
        if(A[res]==A[i]):
            co+=1
        else:
            co-=1
            
        if(co==0):
            res=i
            co+=1
            
    count=0
    for j in range(n):
        if(A[j]==A[res]):
            count+=1
            
    if(count>(N//2)):
        return A[res]
    else:
        return -1



import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            
            print(majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
