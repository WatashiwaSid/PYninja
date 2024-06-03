def stringreverse(str):
    reverse = ""
    for i in str:
        reverse = i + reverse
    
    return reverse

string = input("Enter a valid string: ")
print(f"Original String: {string}")
print(f"Reversed String: {stringreverse(string)}")