import glob

# Initialize total sum
total_sum = 0

for filename in glob.glob("output_*.txt"): 
    with open(filename, "r") as f:
        try:
            total_sum += int(f.read().strip())
        except ValueError:
            print(f"Skipping invalid content in {filename}")

# Print the total sum
print(f"Total sum of random numbers: {total_sum}")

# Save the result
with open("sum_output.txt", "w") as f:
    f.write(str(total_sum))
