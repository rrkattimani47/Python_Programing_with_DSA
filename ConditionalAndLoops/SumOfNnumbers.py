"""
Given an integer n, find and print the sum of numbers from 1 to n.
Note : Use while loop only.
Input Format :
Integer n
Output Format :
Sum
Constraints :
1 <= n <= 100
Sample Input :
10
Sample Output :
55
"""


# Read input as sepcified in the question
# Print output as specified in the question
n=int(input())
count=1
sum=0
while count <= n:
    sum=sum+count
    count=count+1
print(sum)
