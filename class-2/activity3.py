first_name = "Aditya"
last_name = "Suthar"
full_name = first_name + last_name
example = "Haa" * 5

stringResults = {
    "FirstName": first_name,
    "LastName": last_name,
    "FullName": full_name,
    "StringMultiplied5Times": example
}

word = "Coding"

stringDetails = {
    "LengthOfString": len(word),
    "FirstLetter": word[0],
    "LastLetter": word[5],
    "StringSliced": word[:3],
    "WordAdded": word[:3] + "e"
}

print("String Variables:")
for key, value in stringResults.items():
    print(f"  {key}: {value}")

print("\nString Details:")
for key, value in stringDetails.items():
    print(f"  {key}: {value}")