with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()

with open('file.txt', 'r') as file:
    print(f"Read File Content in Parts")
    print(file.read(8))
    file.close()

with open('file.txt', 'a') as file:
    file.write("\nFUN FACT: I don't have instagram.")
    file.close()