"""
Does s contain t ?
Send Feedback
Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
Return true or false.
Do it recursively.
E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.
Input Format :
Line 1 : String s
Line 2 : String t
Output Format :
true or false
Sample Input 1 :
abchjsgsuohhdhyrikkknddg
coding
Sample Output 1 :
true
Sample Input 2 :
abcde
aeb
Sample Output 2 :
false"""

def contains(s,t,lenS,lenT):
    #Implement This Function Here
	if lenT==0:
		return True

	if lenS==0:
		return False
    
	if(s[lenS-1]==t[lenT-1]):
		return contains(s,t,lenS-1,lenT-1)
    
	else:
		return contains(s,t,lenS-1,lenT)
    
s = input()
t = input()

lenS=len(s)
lenT=len(t)

ans = contains(s,t,lenS,lenT)
if ans is True:
    print('true')
else:
    print('false')
