# 7. Break Amount into 1000s, 500s, and Remaining Change 
# Question: Break the total amount into denominations. - Input: - Amount = 3700 - Output: - 
# 1000s: 3 - 500s: 1 - Remaining: 200
#Solution: 
amount = 3700 
thousands = amount//1000 
amount = amount%1000 
five_hundreds = amount//500 
amount = amount%500 
remaining = amount 
print("1000's:", thousands) 
print("500's:", five_hundreds) 
print("remaining:", remaining) 