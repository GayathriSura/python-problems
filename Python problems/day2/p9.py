''' 9. Student Pass if Passed Any Two Subjects 
Question: Check if the student passed any two out of three subjects. Explanation: Use a 
counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, 
Chemistry = 36 - Output: Pass '''

#Solution: 
maths = int(input("enter maths marks: ")) 
physics = int(input("enter physics marks: "))
chemistry = int(input("enter chemistry marks: "))
count = 0 
if maths >= 35: 
    count += 1 
if physics >= 35: 
    count += 1 
if chemistry >= 35: 
    count += 1 
if count >= 2: 
    print("Pass") 
else: 
    print("Fail") 