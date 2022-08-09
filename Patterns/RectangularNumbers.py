"""
Print the following pattern for the given number of rows.
Pattern for N = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
3
Sample Output :
33333
32223
32123
32223
33333
"""
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

for i in range(1, n+1, 1):
    for up in range(1, i, 1):
        print(n-up+1,end = '')
        
    for j in range(i, 2*n-i+1, 1):
        print(n-i+1,end = '')
    
    for lp in range(2*n-i, 2*n-1, 1):
        print(lp-n+2,end = '')
    
    print()


for i in range(n-1, 0, -1):
    for up in range(1, i, 1):
        print(n-up+1,end = '')
        
    for j in range(i, 2*n-i+1, 1):
        print(n-i+1,end = '')
    
    for lp in range(2*n-i, 2*n-1, 1):
        print(lp-n+2,end = '')
    
        
    print()
