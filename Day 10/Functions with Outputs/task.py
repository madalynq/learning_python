def format_name(f_name, l_name):
    formatted_f_name = (f_name.title())
    formatted_l_name = (l_name.title())

    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("anGEla", "YU")



def function_1(text):
    return text + text
# if we placed "hello" into this function and then printed the return, we would get "hellohello"
def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
# you can nest functions using returns because it stores/ keeps the output in the return.
# saving to a new variable and printing:
print(output)
# should return "Hellohello" because the actions of both functions were carried out