# 8. Convert Seconds into Hours, Minutes, and Seconds 
# Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total 
# seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12 
#Solution: 
total_seconds = 3672 
hours = total_seconds//3600 
minutes = (total_seconds%3600)//60 
seconds = total_seconds%60 
print("Hours:",hours) 
print("minutes:",minutes) 
print("seconds:",seconds) 