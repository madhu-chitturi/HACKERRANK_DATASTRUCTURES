                                                          Queue using Two Stacks
  
queue=[]
n=int(input())
for i in range(n):
    s=list(input())
    if(s[0]=='1'):
        a=s.index(' ')
        b=s[a+1:]
        c=b[0]
        for j in range(1,len(b)):
            c+=b[j]
        x=int(c)
        queue.append(x)
    elif(s[0]=='2'):
        queue.pop(0)
    else:
        print(queue[0])
            
