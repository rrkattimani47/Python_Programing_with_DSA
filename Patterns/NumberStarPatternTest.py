"""
Print the following pattern for given number of rows.
Input format :
Integer N (Total number of rows)
Output Format :
Pattern in N lines
Sample Input :
   5
Sample Output :
 5432*
 543*1
 54*21
 5*321
 *4321
 """

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
lines=n
while(i<=lines):
    j=lines
    while(j>=1):
        if(j!=i):
            print(j,end="")
        else:
            print("*",end="")
        j=j-1
    print("")
    i=i+1
    
