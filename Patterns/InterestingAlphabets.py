"""
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
Input format :
N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 26
Sample Input 1:
8
Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH
Sample Input 2:
7
Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG

"""


## Read input as specified in the question.
## Print output as specified in the question.

n=int(input())
i=n
while(i>=1):
    j=i
    start_char=ord('A')
    s=chr(start_char)
    end_char=chr(start_char+n-1)
    while(j<=n):
        charP=chr(ord(s)+j-1)
        print(charP,end="")
        j=j+1
    print()
    i=i-1
