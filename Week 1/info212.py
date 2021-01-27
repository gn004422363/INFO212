import statistics

# This function read target file and return in list
def read(f):
    # The list intend to store value from target file
    data = []
    
    # Open target file
    line = open(f, "r")
    for l in line:
        # Erase \n
        l = l.replace("\n", "")

        # Append to list
        data.append(l)

    # Convert the data from map to a list
    data = list(map(float, data))
        
    return data
        
        
name = "age.txt"
ageList = read(name)
ageList.sort()
print(ageList)

# First answer
first = min(ageList)
print("1.", first)

# Second answer
sec = max(ageList)
print("2.", sec)

# Third answer
total = sum(ageList)
length = len(ageList)
third = total / length
print("3.", third)

# Fourth answer
med = statistics.median(ageList)
print("4.", med)

# Fifth answer
# Sort in ascending order
ageList.sort()
# Break list in ranges of 20
ageList = ageList[0:20]
print("5.", ageList[-1])