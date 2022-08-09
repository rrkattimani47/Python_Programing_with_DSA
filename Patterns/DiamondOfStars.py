"""
Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5



The dots represent spaces.



Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *
  """

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
m = n//2 + 1
for i in range(1, m+1, 1):
    for sp in range(m-i):
        print(' ',end = '')
        
    for j in range(2*i - 1):
        print('*', end = '')
        
    print()
    
for i in range(1, m, 1):
    for sp in range(i):
        print(' ', end = '')
        
    for j in range(1,n-2*i + 1, 1):
        print('*', end ='')
    print()
