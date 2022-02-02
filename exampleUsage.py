import faker
import cards

cc = cards.number

defFunc = faker.firstName()
firstName = faker.randomFirstName

defLastFunc = faker.lastName()
lastName = faker.randomLastName

print("Name: " + firstName + " " + lastName)
print("Number: " + cc + "\nCCV: " + cards.ccv)
