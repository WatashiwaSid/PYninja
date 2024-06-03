#Check if a string contains a substring.
def hassubtring(string,substring):
    if substring in string:
        print(f"Substring {substring} is present")
    else:
        print(f"Substring {substring} is absent")
    
string = input("Enter a valid string: ")
substring = input("Enter substring to look: ").lower()
hassubtring(string,substring)