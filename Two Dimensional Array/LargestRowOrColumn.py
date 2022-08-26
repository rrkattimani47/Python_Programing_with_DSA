"""
For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.
Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.
Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.
Output Format :
For each test case, If row sum is maximum, then print: "row" <row_index> <row_sum>
OR
If column sum is maximum, then print: "column" <col_index> <col_sum>
It will be printed in a single line separated by a single space between each piece of information.

Output for every test case will be printed in a seperate line.
 Consider :
If there doesn't exist a sum at all then print "row 0 -2147483648", where -2147483648 or -2^31 is the smallest value for the range of Integer.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec
Sample Input 1 :
1
2 2 
1 1 
1 1
Sample Output 1 :
row 0 2
Sample Input 2 :
2
3 3
3 6 9 
1 4 7 
2 8 9
4 2
1 2
90 100
3 40
-10 200
Sample Output 2 :
column 2 25
column 1 342
"""
'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    
    sumCol, indexCol = funcCol(arr, nRows, mCols)
    sumRow, indexRow = funcRow(arr, nRows, mCols)
    
    if(sumCol == -1 and sumRow == -1):
        print("row 0 -2147483648")
    elif(sumCol > sumRow):
        print("column", end=" ")
        print(indexCol, end=" ")
        print(sumCol)
    else:
        print("row", end=" ")
        print(indexRow, end=" ")
        print(sumRow)

        
def funcCol(arr, nRows, mCols):
    max_sum=-1
    max_col_index=-1
    for j in range(mCols):
        sum=0
        for i in range (nRows):
            sum+=arr[i][j]
            if sum > max_sum:
                max_col_index=j
                max_sum = sum
    return max_sum, max_col_index


def funcRow(arr, nRows, mCols):
    max_sum=-1
    max_row_index=-1
    for i in range(nRows):
        sum=0
        for j in range (mCols):
            sum+=arr[i][j]
            if sum>max_sum:
                max_row_index=i
                max_sum = sum
    return max_sum, max_row_index


























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
