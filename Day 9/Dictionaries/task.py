programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#print(programming_dictionary)

#adding to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

empty_dictionary = {}


#wipe an existing dictionary
#programming_dictionary = {}

#edit existing value
#if there is no key that matches, it will add a new one
programming_dictionary["Bug"] = "A moth in your computer"

#loop through dictionary
for thing in programming_dictionary:
    print(thing)
    #only prints keys, should put 'for key in dictionary'
    print(programming_dictionary[thing])
    #will include values


#coding exercise: grading program
# convert scores to grades

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
#start converting:

student_grades = {}
for key in student_scores:
    score = student_scores[key]
    if 91 < score < 100:
        grade = "Outstanding"
    elif 81 < score < 90:
        grade = "Exceeds Expectations"
    elif 71 < score < 80:
        grade = "Acceptable"
    elif score <= 70:
        grade = "Fail"
    student_grades[key] = grade

print(student_grades)