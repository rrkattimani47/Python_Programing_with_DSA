"""
Print the following pattern
Pattern for N = 4



The dots represent spaces.



Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1 :
3
Sample Output 1 :
   *
  *** 
 *****
Sample Input 2 :
4
Sample Output 2 :
    *
   *** 
  *****
 *******
 """
n=int(input())
i=1
while(i<=n):
    space=1
    while(space<=n-i):
        print(" ",end="")
        space=space+1
    j=1
    p=1
    while(j<=i):
        print("*",end="")
        j=j+1
    p=i-1
    while(p>=1):
        print("*",end="")
        p=p-1
    print()
    i=i+1
