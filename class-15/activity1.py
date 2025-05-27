with open("codingal.txt", "w") as file:
    file.write("Hello, I have created a file named codingal.txt using Python to write text in it.")
    file.close()

with open("codingal.txt", "r") as file:
    content = file.read()
    print("Words in the file:")
    for line in content.splitlines():
        for word in line.split():
            print(word)
    file.close()