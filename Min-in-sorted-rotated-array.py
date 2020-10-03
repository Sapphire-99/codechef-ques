
def minNumber(arr,low,high):
    #Your code here
    while(low<high):
        mid=int((low+high)/2)
        if(mid>0 and arr[mid-1]>arr[mid]):
            return arr[mid]
        if(arr[mid]>arr[high]):
            low=mid+1
        else:
            high=mid
    return arr[high]



import math


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            print(minNumber(A,0,N-1))
            
            T-=1


if __name__ == "__main__":
    main()

