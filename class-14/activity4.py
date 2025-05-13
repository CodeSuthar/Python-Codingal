with open('file.txt', 'r') as file:
    content = file.read()

    with open('fileUpdated2.txt', 'w') as file_updated:
        # write only odd lines
        file_updated.write("")
        for i, l in enumerate(content.splitlines()):
            if i % 2 == 0:
                file_updated.write(l + "\n")
        file_updated.close()
    file.close()

with open('fileUpdated2.txt', 'r') as file_updated:
    print(f"Read File Content in Parts")
    print(file_updated.read())
    file_updated.close()