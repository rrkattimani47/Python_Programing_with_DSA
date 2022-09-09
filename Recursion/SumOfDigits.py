"""
Write a recursive function that returns the sum of the digits of a given integer.
Input format :
Integer N
Output format :
Sum of digits of N
Constraints :
0 <= N <= 10^9
Sample Input 1 :
12345
Sample Output 1 :
15
Sample Input 2 :
9
Sample Output 2 :
9
"""
## Read input as specified in the question.
## Print output as specified in the question.
def sum(n):
    if(n==0):
        return 0
    
    return (n%10+sum(int(n/10)))
    
    
n=int(input())

print(sum(n))
