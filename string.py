name = input("Enter your name: ")

print("Original string:", name)

print("Length of the string:", len(name))

print("Uppercase:", name.upper())

print("Lowercase:", name.lower())

print("Reversed string:", name[::-1])

print("Is alphanumeric?", name.isalnum())

print("Occurrences of 'a':", name.count('a'))

print("Replace 'a' with '@':", name.replace('a', '@'))
