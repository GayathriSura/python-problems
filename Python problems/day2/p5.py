'''5. Divisible by 2, 3, and 6 
Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is 
divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy '''

#Solution: 
Number = int(input("enter number: "))
if Number%2 == 0 and Number%3 == 0: 
    print("satisfy") 
else: 
    print("not satisfy") 
