"""
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
        1
      212
    32123
  4321234
543212345
"""

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1

while i <= n:
    space = 1
    while space <= n-i:
        print(' ',end ='')
        space = space + 1
        
    p = i
    j = 1
    
    while j <= i:
        print(p, end ='')
        p = p - 1
        j = j + 1
        
    p = 2
    while p <= i:
        print(p, end ='')
        p = p + 1
    
    print()
    i = i + 1
