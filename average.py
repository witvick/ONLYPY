def average(l):
    sum=0

    for i in l:
        sum=sum+i

        ans=sum/len(l)
    return ans

l=[10,20,30,40,50]
ans=average(l)
print ("Average of numbers is:\n",ans)