import random

# Function to display the room
def display(room):
    for i in room:
        print(i)
    print()

# Initialize the room as a 4x4 grid, all elements set to 1 (dirty)
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

print("All the rooms are dirty")
display(room)

# Randomly dirty some rooms
x = 0
y = 0

while x < 4:  # Loop over rows
    while y < 4:  # Loop over columns
        room[x][y] = random.choice([0, 1])  # 0 = clean, 1 = dirty
        y += 1
    x += 1
    y = 0

print("Before cleaning the room, I detect all of these random dirts")
display(room)

# Initialize counters for cleaning
x = 0
y = 0
z = 0  # Counter for dirty cells cleaned

# Clean the room
while x < 4:
    while y < 4:
        if room[x][y] == 1:
            print("Vacuum in this location now:", x, y)
            room[x][y] = 0
            print("Cleaned:", x, y)
            z += 1
        y += 1
    x += 1
    y = 0

# Calculate performance
performance = (100 - ((z / 16) * 100))

print("Room is clean now. Thanks for using the Robot Vacuum Cleaner!")
display(room)

print("Performance =", performance, "%")