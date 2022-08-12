"""
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
"""
## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
star=1
i=1
while(i<=n):
    j=1
    while(j<=2*n+1):
        if(star==i and star==j):
            print("*",end="")
            star=star+1

        elif(j==n+1 or j==2*n+2-i):
            print("*",end="")
        else:
            print(0,end="")
        j=j+1
    print()
    i=i+1
