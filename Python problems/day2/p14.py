'''14. Second Biggest Among Three Numbers 
Question: Find the second largest number among three inputs. Explanation: Use sorting or 
nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: 
Second biggest: 18 '''

#Solution: 
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
if (A > B and A < C) or (A > C and A < B):
    second = A
elif (B > A and B < C) or (B > C and B < A):
    second = B
else:
    second = C
print("Second biggest:", second)

# Or

a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C: "))
if a>b and a>c:
    if b>c:
        print("Second greatest:",b)
    else:
        print("Second greatest:",c)
elif b>a and b>c:
    if a>c:
        print("Second Greatest:",a)
    else:
        print("Second Greatest:",c)
else:
    if a>b:
        print("Second Greatest:",a)
    else:
        print("Second Greatest:",b)