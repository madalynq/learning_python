student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

##create a variable to store the "current" greatest number as it loops through all the variables in the list