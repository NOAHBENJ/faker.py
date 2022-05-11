import names
import random
import cards

# Amount of first names in list "21985"
# This will generate a First Name from the list in names.py called 'firstNames[]'
def firstName():
    global randomFirstName
    # Grabs list of names from names.py firstNames[] list
    first_names = names.firstNames
    # Gets a random index with random.randint() func
    randomFirstName = first_names[random.randint(0, 21985)]
    
    return randomFirstName

# Amount of last names in list "21983"
# pretty much the same as firstName(), but instead looks and grabs a random index from the lastnames list
def lastName():
    global randomLastName

    last_names = names.firstNames
    randomLastName = last_names[random.randint(0, 21983)]
    
    return randomLastName

# Creates function Card()
def Card():
    global fullName

    # Gets list of first names, gets random index
    first_names = names.firstNames
    randomFirstName = first_names[random.randint(0, 21985)]

    # Gets list of last names, gets random index
    last_names = names.firstNames
    randomLastName = last_names[random.randint(0, 21983)]

    # Puts both names together
    randomFullName = randomFirstName + " " + randomLastName

    # Calls the functions in the card file to generate 16 numbers then 3
    cc = cards.number
    ccv = cards.ccv

    # Puts it all together
    randomCard = "Name: " + randomFullName + "\nCard: " + cc + "\nCCV: " + ccv

    return randomCard
