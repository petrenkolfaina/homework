import string
def change(l):
    result = ""
    for i in l:
        if i in string.ascii_uppercase:
            result += i.lower()
        elif i in string.ascii_lowercase:
            result += i.upper()
        else:
            result += i
    return result

l = input("Enter your line: ")
changed_string = change(l)
print(f"Line with changes: {changed_string}")
