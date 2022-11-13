                                                          Balanced Brackets

def brace(s):
    stack=[]
    a=list(s)
    n=len(a)
    if(n==1):
        return 0
    else:
        for i in range(n):
            if(a[i]=='('):
                stack.append(a[i])
            elif(a[i]==')'):
                if(len(stack)!=0):
                    if(stack[(len(stack)-1)]=='('):
                        stack.pop()
                    else:
                        return 0
                else:
                    return 0
            if(a[i]=='{'):
                stack.append(a[i])
            elif(a[i]=='}'):
                if(len(stack)!=0):
                    if(stack[(len(stack)-1)]=='{'):
                        stack.pop()
                    else:
                        return 0
                else:
                    return 0
            if(a[i]=='['):
                stack.append(a[i])
            elif(a[i]==']'):
                if(len(stack)!=0):
                    if(stack[(len(stack)-1)]=='['):
                        stack.pop()
                    else:
                        return 0
                else:
                    return 0
        if(len(stack)==0):
            return 1
        else:
            return 0
    
n=int(input())
for _ in range(n):
    s=input()
    if(brace(s)==1):
        print("YES")
    else:
        print("NO")
    
