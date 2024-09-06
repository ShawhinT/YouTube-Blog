# ceremonial first program
print("Hello, world!")

# for loops
# ---------
# a simple for loop iterating over a sequence of numbers
for i in range(5):
    # print ith element
    print(i)

# for loop iterating over a list
user_interests = ["AI", "Music", "Bread"]

for interest in user_interests:
    # print each item in list
    print(interest)

# for loop iterating over items in a dictionary
user_dict = {"Name":"Shaw", "Age":29, "Interests":["AI", "Music", "Bread"]}

for key in user_dict.keys():
    # print each key and corresponding value
    print(key, "=", user_dict[key])


# if-else
# -------
# check if user is 18 or older
if user_dict["Age"] >= 18:
    print("User is an adult")

# check if user is 1000 or older, if not print they have much to learn
if user_dict["Age"] >= 1000:
    print("User is wise")
else:
    print("User has much to learn")

# count the number of users interested in bread
user_list = [{"Name":"Shaw", "Age":29, "Interests":["AI", "Music", "Bread"]}, {"Name":"Ify", "Age":27, "Interests":["Marketing", "YouTube", "Shopping"]}]
count = 0

for user in user_list:
    if "Bread" in user["Interests"]:
        count = count + 1

print(count, "user(s) interested in Bread")

# count the number of users interested in an arbritrary topic
count = 0
topic = "Antiquing"

for user in user_list:
    if topic in user["Interests"]:
        count = count + 1

print(f"{count} user(s) interested in {topic}")


# basic functions
# ---------------
# print(), a function we've used several times already
for key in user_dict.keys():
    print(key, ":", user_dict[key])


# type(), getting the data type of a variable
for key in user_dict.keys():
    print(key, ":", type(user_dict[key]))


# since len() is not defined for ints we can skip it
for key in user_dict.keys():
    # skips ints
    if type(user_dict[key]) is int:
        continue
    
    print(key, "length :", len(user_dict[key]))


# string methods
# --------------
# make string all lowercase
print(user_dict["Name"].lower())

# make string all uppercase
print(user_dict["Name"].upper())

# split string into list based on a specific character sequence
print(user_dict["Name"].split("ha"))

# replace a character sequence with another
print(user_dict["Name"].replace("w", "whin"))

# list methods
# ------------
# add an element to the end of a list
user_dict["Interests"].append("Entrepreneurship")
print(user_dict["Interests"])

# remove a specific element from a list
user_dict["Interests"].pop(0)
print(user_dict["Interests"])

# insert an element into a specific place in a list
user_dict["Interests"].insert(1, "AI")
print(user_dict["Interests"])

# dict methods
# ------------
# accessing dict keys
print(user_dict.keys())

# accessing dict values
print(user_dict.values())

# accessing dict items
print(user_dict.items())

# removing a key
user_dict.pop("Name")
print(user_dict.items())

# adding a key
user_dict["Name"] = "Shaw"
print(user_dict.items())

# user-defined functions
# ----------------------
def user_description(user_dict):
    """
        Function to return a sentence (string) describing input user
    """
    return f'{user_dict["Name"]} is {user_dict["Age"]} years old and is interested in {user_dict["Interests"][0]}.'

# print user description
description = user_description(user_dict)
print(description)

# print description for a new user!
new_user_dict = {"Name":"Ify", "Age":27, "Interests":["Marketing", "YouTube", "Shopping"]}
print(user_description(new_user_dict))


def interested_user_count(user_list, topic):
    """
        Function to count number of users interested in an arbitrary topic
    """
    count = 0

    for user in user_list:
        if topic in user["Interests"]:
            count = count + 1
    
    return count

# define user list and topic
user_list = [user_dict, new_user_dict]
topic = "Shopping"

# compute interested user count and print it
count = interested_user_count(user_list, topic)
print(f"{count} user(s) interested in {topic}")