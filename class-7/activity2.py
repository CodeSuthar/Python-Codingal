dictionary = {
    'name': 'Aditya K. Suthar',
    'aka': 'CodeSuthar',
    'age': 15,
    'location': 'India',
    'hobbies': ['Coding', 'Reading', 'Watching Movies & Thriller Series'],
    'languages': ['Python', 'HTML', 'CSS', 'JavaScript', 'Java', 'C++'],
    'tools': ['VS Code', 'PyCharm'],
    'socials': {
        'github': 'https://github.com/CodeSuthar',
        'instagram': 'https://instagram.com/CodeSuthar',
        'website': 'https://codesuthar.is-a.dev'
    },
    0: 'This is a key with integer value'
}

print("-----------------")
print(f"| - 1. Printing Dictionary: {dictionary}")
print(f"| - 2. Printing a specific key: {dictionary['name']}")
print(f"| - 3. Printing a specific key: {dictionary['age']}")
print("-----------------")

dictionary['age'] = 16
print(f"| - 4. Update: {dictionary}")

dictionary['FavShow'] = "C.I.D"
print(f"| - 5. Add: {dictionary}")

dictionary.pop(0)
print(f"| - 6. Pop: {dictionary}")

dictionary.clear()
print(f"| - 7. Clear: {dictionary}")
print("-----------------")