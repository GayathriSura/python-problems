'''10. Biggest Among Three Numbers 
Question: Find the biggest number among three. Explanation: Compare each pair of 
numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9 '''

#Solution: 
A = int(input("enter A: "))
B = int(input("enter B: "))
C = int(input("enter C: "))
if A>B and A>C: 
    print("biggest is:,",A) 
elif B>A and B>C: 
    print("biggest is:",B) 
else: 
    print("biggest is:",C) 