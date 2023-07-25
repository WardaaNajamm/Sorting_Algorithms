def adv_countsort(A,n,l,r):
    n=max(A)+1
    count=[0]*n
    for i in A:
        count[i]+=1
    
    for i in range(1,max(A)):
        count[i]=count[i]+count[i-1]
    
    output=count[l-1]-count[r]
    print("Numbers in given range: ")
    print(output)

# A={34,56,78,23,12,2,5,6,7,8,43,2,3,4,5,67,12,45}
# a=input("Enter lower bound value: ")
# b=input("Enter upper bound value: ")
# adv_countsort(A, len(A), a,b)
