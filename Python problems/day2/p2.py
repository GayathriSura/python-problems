'''2. Divisible by 5 but Not by 10 
Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) 
to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: 
Satisfy '''

#Solution: 
Number = int(input("enter number: "))
if (Number%5==0) and (Number%10!=0): 
    print("satisfy") 
else: 
    print("not satisfy") 