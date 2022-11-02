LINK: https://www.hackerrank.com/challenges/maximum-element/problem

You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Function Description

Complete the getMax function in the editor below.

getMax has the following parameters:
- string operations[n]: operations as strings

Returns
- int[]: the answers to each type 3 query

Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query.

Sample Input

STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91

<============================= PYTHON CODE ================================>

n=int(input())
stack=[]
maxstack=[]
for i in range(n):

    str1=list(input())
    if (str1[0]=='1'):
        a=str1.index(' ')
        b=str1[a+1:]
        x=b[0]
        for j in range(1,len(b)):
            x+=b[j]
        stack.append(int(x))
        if(len(maxstack)==0):
            max1=int(x)
            maxstack.append(max1)   
        else:
            z=len(maxstack)
            max1=max(int(x),maxstack[z-1])
            maxstack.append(max1) 
           
    elif(str1[0]=='2'):
        if(len(maxstack)>0):
            maxstack.pop()
        if(len(stack)>0):
            stack.pop()
    else:
        z=len(maxstack)
        print(maxstack[z-1])
                    
