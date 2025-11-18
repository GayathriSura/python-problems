'''11. Smallest Among Three Numbers 
Question: Find the smallest number among three. Explanation: Use comparison logic to 
determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4 '''

#Solution: 
A = int(input("enter A: "))
B = int(input("enter B: "))
C = int(input("enter C: "))
if A<B and A<C: 
    print("smallest is:,",A) 
elif B<A and B<C: 
    print("smallest is:",B) 
else: 
    print("smallest is:",C) 