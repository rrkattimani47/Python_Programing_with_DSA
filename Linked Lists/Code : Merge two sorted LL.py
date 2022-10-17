"""
Code : Merge two sorted LL
Send Feedback
You have been given two sorted(in ascending order) singly linked lists of integers.
Write a function to merge them in such a way that the resulting singly linked list is also sorted(in ascending order) and return the new head to the list.
Note :
Try solving this in O(1) auxiliary space.

No need to print the list, it has already been taken care.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the first sorted singly linked list separated by a single space. 

The second line of the input contains the elements of the second sorted singly linked list separated by a single space. 
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output :
For each test case/query, print the resulting sorted singly linked list, separated by a single space.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t = 10^2
0 <= N <= 10 ^ 4
0 <= M <= 10 ^ 4
Where N and M denote the sizes of the singly linked lists. 

Time Limit: 1sec
Sample Input 1 :
1
2 5 8 12 -1
3 6 9 -1
Sample Output 1 :
2 3 5 6 8 9 12 
Sample Input 2 :
2
2 5 8 12 -1
3 6 9 -1
10 40 60 60 80 -1
10 20 30 40 50 60 90 100 -1
Sample Output 2 :
2 3 5 6 8 9 12 
10 10 20 30 40 40 50 60 60 60 80 90 100
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def LinkedLists(arr):
    head=None
    tail=None
    for i in arr:
        if i==-1:
            break
        data = Node(i)
        if head is None:
            head=data
            tail=data
        else:
            tail.next=data
            tail=data
    return head

def MergeSortedLL(head1,head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    mergedHead = None
    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next
    mergedTail = mergedHead


    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    return mergedHead





def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head=head.next

def printReverse(head) :
    prev = None
    current = head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    printLL(head)

n=int(input()) 
for i in range(n):
	arr1 = list(map(int, input().split()))
	arr2 = list(map(int, input().split()))

printLL((MergeSortedLL(LinkedLists(arr1),LinkedLists(arr2))))
