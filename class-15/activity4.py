
with open("new.txt", "r") as file:
    data1 = file.read()

with open("eliminationOutput.txt", "r") as file:
    data2 = file.read()

with open("newOutput.txt", "w") as file:
    file.write(data1 + "\n" + data2)
print("Data from 'new.txt' and 'eliminationOutput.txt' has been combined into 'newOutput.txt'.")
print("Content of 'newOutput.txt':")
with open("newOutput.txt", "r") as file:
    for line in file:
        print(line.strip())