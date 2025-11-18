'''13. Cars Required for Members (Max 5 per car) 
Question: Calculate how many cars are needed for a given number of people. Explanation: 
Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: 
Cars needed = 4 '''

#Solution: 
n = int(input("Enter members:"))
if n%5 == 0:
    print("cars required", n//5)
else:
    print("cars required", n//5+1)