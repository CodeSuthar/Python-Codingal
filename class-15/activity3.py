lines_seen_so_far = set()

print("Eliminating duplicates from the file...")

with open("eliminationOutput.txt", "w") as output_file:
    with open("repeated.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line not in lines_seen_so_far:
                lines_seen_so_far.add(stripped_line)
                output_file.write(line)
                print(f"Writing line to output file: {stripped_line}")
            else:
                print(f"Duplicate line found: {stripped_line} - not writing to output file.")

print("Duplicates have been eliminated from the file.")

print("\nContent of the file after eliminating duplicates:")
with open("eliminationOutput.txt", "r") as output_file:
    for line in output_file:
        print(line.strip())