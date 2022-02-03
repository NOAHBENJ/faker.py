import faker
import cards

# Getting the first name process to run, if you don't do that, then firstname will not work, it will be null or error.
defFunc = faker.firstName()
firstName = faker.randomFirstName

# Getting the card, same as comment above
defCardFunc = faker.Card()
Card = faker.randomCard

# Getting the last name, same as comment above
defLastFunc = faker.lastName()
lastName = faker.randomLastName

# Printint all the variables, you can modify this how you want, this is just an example, you dont need this many arguments when printing, i just do to make it look nice
print("Name: " + firstName + " " + lastName)

# With this print, unlike the above lines, this one has all the nice printing done for you.
print(Card)
