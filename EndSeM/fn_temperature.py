def tofahrenheit(cel):
    return ((9/5)*cel) + 32


temp = int(input("Enter temperature in celsius: ")) 
print(f"Temperature in fahrenheit: {tofahrenheit(temp)}")