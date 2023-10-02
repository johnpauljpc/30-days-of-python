# Create list
myList = [2,3,4,5,6,44,2]

# Get the length of a list
len(myList)

# Get the sum of the list items
sum(myList)

# Add item to a list
myList.append(20)

# Delete item from a list
myList.pop() #removes the last item
myList.pop(2) #removes list item in position 2

# Modify a List item
myList[1] = "modified"


# Dictionary  #

# create a dictionary
myDict = {"key1": "value1", "name":"Johnpaul", "age":25, "profession": "web developer"}

# How to access an item
myDict["age"] #Displays 25
list(myDict.values())[2] # Outputs the value in postion 2
list(myDict.keys())[2]  # Outputs the key in position 2

# How to access the list of the values of a dictionary
list(myDict.values())

# How to access the list of the keys of a dictionary
list(myDict.keys())

# How to add item to a dictionary
myDict["key_name"] = "value"

# How to delete an item from a dictionary
myDict.pop("key1") #Deletes the item in the specified position(key)

# How to modify a value
myDict["name"] = "Johnpaul Chigozie"

