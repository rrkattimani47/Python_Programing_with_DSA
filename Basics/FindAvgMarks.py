"""
Write a program to input marks of three tests of a student (all integers). Then calculate and print the average of all test marks.
Input format :
3 Test marks (in different lines)
Output format :
Average 
Sample Input 1 :
3 
4 
6
Sample Output 1 :
4.333333333333333
Sample Input 2 :
5 
10 
5
Sample Output 2 :
6.666666666666667
"""

test1=int(input())
test2=int(input())
test3=int(input())

average=(test1+test2+test3)/3

print(average)
