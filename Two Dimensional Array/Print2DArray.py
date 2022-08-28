"""
Given a 2D integer array with n rows and m columns. Print the 0th row from input n times, 1st row n-1 times…..(n-1)th row will be printed 1 time.
Input format :
Line 1 : No of rows (n) and no of columns (m) (separated by single space)
Line 2 : Row 1 elements (separated by space)
Line 3 : Row 2 elements (separated by space)
Line 4 : and so on
Sample Input 1:
3 3
1 2 3
4 5 6
7 8 9
Sample Output 1 :
1 2 3
1 2 3
1 2 3
4 5 6
4 5 6
7 8 9
"""
## Read input as specified in the question.
## Print output as specified in the question.
def twoDArray(n,m,li):
    for i in range(n):
        k=1
        while(k<=n-i):
            for j in range(m):
                print(li[i][j],end =" ")
            print()
            k=k+1
    		
s=input().split()
n,m=int(s[0]),int(s[1])
li=[[int(j) for j in input().split() ]for i in range(n) ]
twoDArray(n,m,li)
