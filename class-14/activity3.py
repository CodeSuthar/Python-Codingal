with open('file.txt', 'r') as file:
    content = file.read()

    with open('fileUpdated.txt', 'w') as file_updated:
        file_updated.write("")
        for line in content.splitlines():
            if not line.startswith("I am"):
                file_updated.write(line + "\n")
        file_updated.close()
    file.close()

with open('fileUpdated.txt', 'r') as file_updated:
    print(f"Read File Content in Parts")
    print(file_updated.read())
    file_updated.close()