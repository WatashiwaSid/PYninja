#Count occurence of a charcter in a string.
def countchar(str, char):
    count=0
    for i in str:
        if(i==char):
            count=count+1
    
    return count

string = input("Enter a valid string: ")
char = input("Enter character to count in string: ").lower()
print(f"{char} was found {countchar(string,char)} times.")