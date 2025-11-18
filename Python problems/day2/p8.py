'''8. Student Pass if Passed Any One Subject (>= 35) 
Question: Check if the student passed at least one subject. Explanation: Use logical OR 
to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 
25 - Output: Pass '''

#Solution: 
maths = int(input("enter maths marks: ")) 
physics = int(input("enter physics marks: "))
chemistry = int(input("enter chemistry marks: "))
if maths>=35 or physics>=35 or chemistry>=35: 
    print("pass") 
else: 
    print("fail")