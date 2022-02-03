import random

# Generates 16 numbers, between 0 and 9
I = str(random.randint(0, 9))
II = str(random.randint(0, 9))
III = str(random.randint(0, 9))
IV = str(random.randint(0, 9))
V = str(random.randint(0, 9))
VI = str(random.randint(0, 9))
VII = str(random.randint(0, 9))
VIII = str(random.randint(0, 9))
IX = str(random.randint(0, 9))
X = str(random.randint(0, 9))
XI = str(random.randint(0, 9))
XII = str(random.randint(0, 9))
XIII = str(random.randint(0, 9))
XIV = str(random.randint(0, 9))
XV = str(random.randint(0, 9))
XVI = str(random.randint(0, 9))

# Puts all the numbers together, with three spaces in between each cluster of four, to make it look nice like an actual card (BUT THIS WILL NOT WORK, I REPEAT, WILL NOT WORK)
# rather than "5835645473245673", it will look like "5835 6454 7324 5673"
number = I + II + III + IV + " " + V + VI + VII + VIII + " " + IX + X + XI + XII + " " + XIII + XIV + XV + XVI

#Generates 3 numbers, and puts it all together in one line, nice!
ccv = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
