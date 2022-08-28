"""
Given a string S (that can contain multiple words), you need to find the word which has minimum length.
Note : If multiple words are of same length, then answer will be first minimum length word in the string.
Words are seperated by single space only.
Input Format :
String S
Output Format :
Minimum length word
Constraints :
1 <= Length of String S <= 10^5
Sample Input 1 :
this is test string
Sample Output 1 :
is
Sample Input 2 :
abc de ghihjk a uvw h j
Sample Output 2 :
a
"""
## Read input as specified in the question.
## Print output as specified in the question.
s=input()
str=s.split()
min=len(str[0])
min_word=""
for ele in str:
	if(len(ele)<min):
        
		min=len(ele)
		min_word=ele
    
        
print(min_word)
