"""
Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
For eg. N = 5

1        1
12      21
123    321
1234  4321
1234554321
Sample Input 1 :
4
Sample Output 1 :
1      1
12    21
123  321
12344321
"""
n = int(input())
i=1

while i <= n:
    j=1
    while j <= i:
        print(j,end='')
        j = j + 1
        
    sp = 1
    while sp <= 2*(n - i):
        print(' ',end ='')
        sp = sp + 1
        
    p = i
    j = 1
    while j <= i:
        print(p,end = '')
        p = p - 1
        j = j + 1
    
    print()
    i=i+1
