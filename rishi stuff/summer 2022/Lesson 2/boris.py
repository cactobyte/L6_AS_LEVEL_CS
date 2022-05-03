# -*- coding: utf-8 -*-
# # Simple Messages
# Assign a message to a variable, and print that message. Then change the value of your variable to a new message, 
# and print the new message.

message = "Hello"
print(message)
message = "Hello again"
print(message)


# Famous Quote
# Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

# Stripping Names
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, “\t” and “\n”, at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = " \tBoris Cheung \nRishi Bagga"
print(name)
print(name.strip())
print(name.lstrip())
print(name.rstrip())

# Favourite Number
# Use a variable to represent your favourite number. 
# Then, using that variable, create a message that reveals your favourite number. Print that message.

favNumber = 69
print("My favourite number is {}").format(favNumber)

#Names
#Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

names = ["Samsher", "Jack", "Oscar", "Charlie"]
for i in names:
    print(i)

# Greetings
# Start with the list you used in the above exercise, but instead of just 
# printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.

names = ["Samsher", "Jack", "Oscar", "Charlie"]
for i in names:
    print("Hey {}, how are you doing!").format(i)

# Guest List

# If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

invitees = ["Obama", "Trump", "Biden"]
for i in invitees:
    print("Dear {}, would you like to have dinner with me?").format(i)


# Changing Guest List
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# Start with your program from the above exercise. Add a print statement at the end of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print("oh no!, Trump cannot attend, we will have to invite Quandale Dingle instead!")
invitees[1] = "Quandale Dingle"
for i in invitees:
    print("Dear {}, would you like to have dinner with me?").format(i)

# More Guests
# You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# Start with your program from two exercises (guest list) or the above. 
# Add a print statement to the end of your program informing people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list. 
# Print a new set of invitation messages, one for each person in your list.

print("We've found a bigger table, lets invite:")
invitees.insert(0, "John Cena")
invitees.insert(3, "Issac Newton")
invitees.append("Jamal")

for i in invitees:
    print("Dear {}, would you like to have dinner with me?").format(i)

# Shrinking Guest List

# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# Start with your program from the above. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.

print("We can only invite 2 people")

for i in invitees:
    if i < 4:
        print("You have been uninvitied {}, off you pop").format(i)
        invitees.pop(i)
    else:
        print("You are still invited, {}, make sure your not late").format(i)
    
del invitees[-2]
print(invitees)

# Seeing the World

# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

places = ["Wales", "Germany", "Japan", "South Korea", "Canada"]
print(places) 
sorted(places)
print(places)
sorted(places, reverse=True)
print(places)

places.reverse()
print(list)
places.reverse()
print(list)

places.sort()
print(list)
places.sort(reverse=True)
print(list)
