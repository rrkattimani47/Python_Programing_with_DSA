"""
Print the following pattern for the given number of rows.
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
         232
       34543
     4567654
   567898765
Sample Input 2:
4
Sample Output 2:
           1
         232
       34543
     4567654
     """

n=int(input())
i=1
while(i<=n):
    space=1
    while(space<=n-i):
        print(" ",end="")
        space=space+1
    j=1
    k=i
    while(j<=i):
        print(k,end="")
        j=j+1
        k=k+1
    j=1
    k=2*i-2
    while(j<=i-1):
        print(k,end="")
        k=k-1 
        j=j+1
    print()
    i=i+1
    
