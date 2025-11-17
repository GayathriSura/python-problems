'''1. Area of Square 
Question: Calculate the area of a square. - Formula: Area = side × side - Input: - Side = 5 - 
Output: - Area of square is: 25'''
#Solution: 
side = 5 
area = side*side 
print("area of square is:",area) 


'''2. Area of Rectangle 
Question: Calculate the area of a rectangle. - Formula: Area = length × breadth - Input: - 
Length = 6 - Breadth = 4 - Output: - Area of rectangle is: 24'''
#Solution: 
length = 6 
breadth = 4 
area = length*breadth 
print("area of rectangle is:",area) 


'''3. Area of Triangle 
Question: Calculate the area of a triangle using base and height. - Formula: Area = (1/2) × 
base × height - Input: - Base = 8 - Height = 5 - Output: - Area of triangle is: 20.0'''
#Solution: 
Base = 8 
Height = 5 
Area = 0.5*Base*Height 
print("area of triangle is:",Area) 


'''4. Perimeter of Square 
Question: Calculate the perimeter of a square. - Formula: Perimeter = 4 × side - Input: - 
Side = 6 - Output: - Perimeter of square is: 24'''
#Solution: 
side = 6 
perimeter = 4*side 
print("perimeter of square is:",perimeter) 


'''5. Perimeter of Rectangle 
Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + 
breadth) - Input: - Length = 5 - Breadth = 3 - Output: - Perimeter of rectangle is: 16'''
#Solution: 
length = 5 
breadth = 3 
perimeter = 2*(length+breadth) 
print("perimeter of rectangle is:",perimeter) 


'''6. Perimeter of Triangle 
Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + 
side3 - Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18'''
#Solution: 
side1 = 5 
side2 = 6 
side3 = 7 
perimeter = side1+side2+side3 
print("perimeter of triangle is:",perimeter) 


'''7. Break Amount into 1000s, 500s, and Remaining Change 
Question: Break the total amount into denominations. - Input: - Amount = 3700 - Output: - 
1000s: 3 - 500s: 1 - Remaining: 200'''
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


'''8. Convert Seconds into Hours, Minutes, and Seconds 
Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total 
seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12 '''
#Solution: 
total_seconds = 3672 
hours = total_seconds//3600 
minutes = (total_seconds%3600)//60 
seconds = total_seconds%60 
print("Hours:",hours) 
print("minutes:",minutes) 
print("seconds:",seconds) 


'''9. Sum of Marks (Maths, Physics, Chemistry) 
Question: Calculate the sum of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - 
Chemistry = 88 - Output: - Total marks: 263'''
#Solution: 
math = 85 
physics = 90 
chemistry = 88 
total_marks = math+physics+chemistry 
print("total marks:",total_marks) 


'''10. Average of Marks (Maths, Physics, Chemistry) 
Question: Calculate the average of marks in 3 subjects. 
- Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67'''
#Solution: 
math = 85 
physics = 90 
chemistry = 88 
total_marks = math+physics+chemistry 
avg = total_marks/3 
print(f"average of marks: {avg:.2f}")


