def sumandavg(list):
    sumi = sum(list)
    avg = sumi/len(list)
    return sumi,avg
    
add,avg = sumandavg([5,10,15,20])
print(f"Sum of list items: {add}")
print(f"Average of list items: {avg}")