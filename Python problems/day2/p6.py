'''6. Voting Eligibility 
Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible 
to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote '''

#Solution: 
age = int(input("enter age:")) 
if age>=18: 
    print("eligible to vote") 
else: 
    print("not eligible to vote") 