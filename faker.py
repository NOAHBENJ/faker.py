import names
import random

# Amount of first names in list "21985"
def firstName():
    global randomFirstName

    first_names = names.firstNames
    randomFirstName = first_names[random.randint(0, 21985)]

try:
    randomFirstName = randomFirstName
except Exception as e:
    pass

# Amount of last names in list "21983"
def lastName():
    global randomLastName

    last_names = names.firstNames
    randomLastName = last_names[random.randint(0, 21983)]

try:
    randomLastName = randomLastName
except:
    pass
