import random

# Generate a random number between 0 and 10
random_number = random.randint(0, 10)

# Save the number to a file
with open("output.txt", "w") as f:
    f.write(str(random_number))

print(f"Generated random number: {random_number}")
