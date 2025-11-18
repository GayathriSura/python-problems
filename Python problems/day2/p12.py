'''12. Perfect Square or Not 
Question: Check if a number is a perfect square. Explanation: A number is a perfect square 
if the square of its square root equals the number. - Input: Number = 49 - Output: Perfect 
square'''

#Solution: 
n= int(input("Enter:"))
s = int(n**0.5)
if s**2 == n:
    print("Perfect square")
else:
    print("Not a perfect square")