"""
Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.
Input format :
Line 1 : Integer M
Line 2 : Integer N
Output format :
M x N
Constraints :
0 <= M <= 1000
0 <= N <= 1000
Sample Input 1 :
3 
5
Sample Output 1 :
15
Sample Input 2 :
4 
0
Sample Output 2 :
0
"""
## Read input as specified in the question.
## Print output as specified in the question.
def product(x,y):
    if x<y:
        return product(y,x)
    elif y!=0:
        return (x+product(x,y-1))
    else:
        return 0
    
m=int(input())
n=int(input())
print(product(m,n))
