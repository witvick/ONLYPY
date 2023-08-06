def distinct(l):
    ans=0

    for i in range(len(l)):
        if(l[i] not in l[0:i]):
            ans=ans+1

    return ans





l=[10,20,10,20,30,50,16]
ans=distinct(l)
print("no of distinct element is:",ans)