import os 
new_file = "new.txt"
file_exists = "codingal.txt"
with open(new_file, "w") as file:
    file.write("Hello, I have created a file named codingal.txt using Python to write text in it.")
    
print("Checking if the file exists...")
if os.path.exists(file_exists):
    print(f"The file '{file_exists}' exists.")
else:
    print(f"The file '{file_exists}' does not exist.")
    with open(file_exists, "w") as file:
        file.write("Hello, I have created a file named codingal.txt using Python to write text in it.")
        print(f"The file '{file_exists}' has been created.")

os.remove("codingal.txt")
print(f"The file '{file_exists}' has been deleted.")

#creating a folder
folder_name = "AFolder"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created.")
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' has been removed.")
else:
    print(f"Folder '{folder_name}' already exists.")
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' has been removed.")
