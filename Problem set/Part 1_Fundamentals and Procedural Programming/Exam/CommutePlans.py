in_a_hurry = True
is_raining = False
have_backpack = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you are deciding how to get to school today. You have
#four options: walk, bike, bus, or drive.
#
#There are three variables that determine which options you
#might choose:
#
# - in_a_hurry: whether you're in a hurry to get to class.
# - is_raining: whether it's raining outside
# - have_backpack: whether you need to carry a backpack
#
#The following rules tell you whether each option is
#possible:
#
# - Walking is an option if it is not raining and you
#   are not in a hurry to get to class.
# - Biking is an option as long as it is not raining,
#   unless you need to carry a backpack.
# - A bus is an option as long as you are not in a hurry
#   to get to class.
# - A car is your last resort: it is only an option if
#   none of the other three are options.
#
#Print True or False for each option, according to the
#following structure:
#
#Walk: False
#Bike: False
#Bus: False
#Car: True


#Add your code here!
walk = not is_raining and not in_a_hurry
bike = not is_raining and not have_backpack
bus = not in_a_hurry
car = not walk and not bike and not bus

print("Walk:", walk)
print("Bike:", bike)
print("Bus:", bus)
print("Car:", car)