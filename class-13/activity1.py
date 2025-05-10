import os
import re
import requests
import tempfile

def geturl(url):
    # Extracting fileid from the URL
    matched = re.search(r"/file/d/([a-zA-Z0-9_-]+)", url)
    if not matched:
        raise ValueError("Invalid URL format")
    
    file_id = matched.group(1)
    download_file_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    return download_file_url

def download_file_to_temp(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        #creating a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    temp_file.write(chunk)
                    print(f"File downloaded to {temp_file.name}")
            return temp_file.name
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")

if __name__ == "__main__":
    url = "https://drive.google.com/file/d/11b0QAQxQ7sgjaObHsy6m50M2WbO0sPqq/view"
    temp_file_path = download_file_to_temp(geturl(url))
    if temp_file_path:
        print(f"File downloaded successfully to {temp_file_path}")
    else:
        print("Failed to download the file.")

    print("Temporary file will be deleted after the program ends.")

    print("==================Options===================")
    print("1. Read the file")
    print("2. Write to the file")
    print("3. Calculate the lines in the file")
    print("4. Append the content of one file to another")
    print("==================Options===================")
    option = input("Enter your choice: ")

    if option == "1":
        with open(temp_file_path, 'rb') as file:
            # Read the file content
            content = file.read()

            # printing the file content by splitting it into lines
            lines = content.splitlines()
            os.system('cls' if os.name == 'nt' else 'clear')
            for line in lines:
                print(line.decode('utf-8'))  # Decode bytes to string
    elif option == "2":
        # Write to the file (overwrite) and then display the new content
        content = input("Enter the content to write to the file: ")
        with open(temp_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print("Content written to the file successfully.")
    
        # Read and display the new content
        with open(temp_file_path, 'r', encoding='utf-8') as file:
            os.system('cls' if os.name == 'nt' else 'clear')
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    elif option == "3":
        with open(temp_file_path, 'rb') as file:
            # Calculate the number of lines in the file
            content = file.read()
            lines = content.splitlines()
            print(f"Number of lines in the file: {len(lines)}")
    elif option == "4":
        # Append a new file to the existing file url i gave you
        new_file_url = input("Enter the URL of the new file to append: ")
        new_file_path = download_file_to_temp(geturl(new_file_url))

        with open(temp_file_path, 'ab') as file:
            with open(new_file_path, 'rb') as new_file:
                # Append the content of the new file to the existing file
                content = new_file.read()
                file.write(content)
                print("Content appended to the file successfully.")
