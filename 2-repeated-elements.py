

def twoRepeated(arr, N):
    
    for i in range(0,N+2) : 
          
        if(arr[abs(arr[i])] > 0) : 
            arr[abs(arr[i])] = (-1) * arr[abs(arr[i])] 
            
        else : 
            print(abs(arr[i]),end = " ") 





import math
    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            twoRepeated(A,N)
            print()
            
            T-=1


if __name__ == "__main__":
    main()

