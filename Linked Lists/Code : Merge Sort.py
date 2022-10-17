"""
Code : Merge Sort
Send Feedback
 Given a singly linked list of integers, sort it using 'Merge Sort.'
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the sorted singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
1
10 9 8 7 6 5 4 3 -1
Sample Output 1 :
 3 4 5 6 7 8 9 10 
 Sample Output 2 :
2
-1
10 -5 9 90 5 67 1 89 -1
Sample Output 2 :
-5 1 5 9 10 67 89 90 
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def findMid(head) :
	if head is None :
		return None

	slow, fast = head, head

	while fast.next is not None and fast.next.next is not None :
		slow = slow.next
		fast = fast.next.next

	return slow


def merge(head1, head2):

    if(head1 is None):
        return head2
    
    if(head2 is None):
        return head1
    
    newHead, newTail = None, None

    if head1.data < head2.data :
        newHead = head1
        newTail = head1
        head1 = head1.next
    else :
        newHead = head2
        newTail = head2
        head2 = head2.next

    while head1 is not None and head2 is not None :
        if head1.data < head2.data :
            newTail.next = head1
            newTail = newTail.next
            head1 = head1.next
        else :
            newTail.next = head2
            newTail = newTail.next
            head2 = head2.next


    if head1 is not None :
        newTail.next = head1

    if head2 is not None :
        newTail.next = head2


    return newHead



def mergeSort(head) :
	if head is None or head.next is None :
		return head

	mid = findMid(head)
	half1 = head
	half2 = mid.next
	mid.next = None

	half1 = mergeSort(half1)
	half2 = mergeSort(half2)

	finalHead = merge(half1, half2)

	return finalHead





def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
