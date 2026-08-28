from collections import deque
string=input("Enter a String:")
dq=deque()
for char in string:
    if char.isalnum():
        dq.append(char.lower())
is_palindrome=True
while len(dq)>1:
    front=dq.popleft()
    rear=dq.pop()
    if front != rear:
        is_palindrome=False
        break
if is_palindrome:
    print("The String is a Palindrome")
else:
    print("The String is not a Palindrome")
