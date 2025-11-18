'''7. Student Pass/Fail Based on All Subjects >= 35 
Question: Check if a student passed all subjects (maths, physics, chemistry). 
Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 
40, Physics = 36, Chemistry = 30 - Output: Fail '''

#Solution:  
maths = int(input("enter maths marks: ")) 
physics = int(input("enter physics marks: "))
chemistry = int(input("enter chemistry marks: "))
if maths>=35 and physics>=35 and chemistry>=35: 
    print("pass") 
else: 
    print("fail")