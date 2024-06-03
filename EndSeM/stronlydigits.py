#Check if a string contains only digits(numbers).
def strictNumericString(string):
    return string.isnumeric()

string = input("Enter a numeric string: ")
if(strictNumericString(string)):
    print("String has only numbers.")
else:
    print("String has characters and numbers.")