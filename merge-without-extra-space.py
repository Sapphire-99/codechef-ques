
def merge(a,n,b,m):
    #code here
    co=0
    i=0
    while(i<m and b[i]<a[n-1]):
        co+=1
        i+=1
    for i in range(co):
        if(b[i]<a[n-1-i] and i<m and i<n):
            b[i],a[n-1-i]=a[n-1-i],b[i]
        else:
            break
    a.sort()
    b.sort()
    





if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        merge(a,n,b,m)
        if(len(a)!=n and len(b)!=m):
            print("Do in O(1) space")
        print(*a,end=" ")
        print(*b)

