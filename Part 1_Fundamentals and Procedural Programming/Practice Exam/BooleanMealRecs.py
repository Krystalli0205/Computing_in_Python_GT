hot = True
cold = False
morning = True
evening = False
night = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a program that will recommend a meal based on the
#current weather and time of day. Specifically, the program
#should recommend:
#
# - soup if it's cold and either evening or night
# - a biscuit if it's morning and cold
# - cereal if it's morning and hot, or whenever the time is
#   night
# - pizza whenever it's either evening or night
#
#Write some code below that will print four lines, one for
#each of the four meals. The lines should look like this:
#
#Soup: False
#Biscuit: False
#Cereal: True
#Pizza: False
#
#The values (True and False) will differ based on the
#values assigned to hot, cold, morning, evening, and night
#at the start of the program.


#Add your code here!
soup = cold and (evening or night)
biscuit = cold and morning
cereal = morning and hot or night
pizza = evening or night

print("Soup: {}".format(soup))
print("Biscuit: {}".format(biscuit))
print("Cereal: {}".format(cereal))
print("Pizza: {}".format(pizza))