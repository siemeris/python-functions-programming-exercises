# Your code goes here:
def render_person(name, birthday, color, years, gender):
    return name + " is a " + str(years) + " years old " + gender + " born in " + str(birthday) + " with " + color + " eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))