bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))    ### "flooring" number, getting rid of all decimals

print(round(bmi))  #round up or down to a whole number based on the "0.1" decimal place, normal rounding rules

print(round(bmi, 2)) ##this will allow you to choose how many decimal places

score = 0
# user scores a point (assignment operators, allows you to add/subtract/multiply/divide to the original
# variable and assign a new value
score +=1
print(score)

## "f-strings"
print("Your score is " + str(score))   #converting types

# f-strings allow for easier conversions with multiple types

height = 1.8
is_winning =True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")