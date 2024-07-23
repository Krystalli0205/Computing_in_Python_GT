total_seconds = 5278

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you are writing the software for a call center. As
#part of this, you need to tell the customer currently on hold
#what their estimated wait time is.
#
#The software that actually generates the estimated wait time
#returns it as a number of seconds. However, telling the customer
#"Your estimated wait time is 5278 seconds" is pretty meaningless.
#Instead, we want to say something like:

#Your estimated wait time is 1 hour(s), 27 minute(s), and 58 second(s).
#
#Add some code that will print that sort of estimated wait time,
#replacing 1, 27, and 58 with the actual numbers derived from the
#variable total_seconds. Remember, there are 60 seconds in a minute,
#and 60 minutes in an hour: you never wawnt to mention more than 60
#minutes (as that would add an hour) or 60 seconds (as that would add
#a minute).


#Add your code here!
hour = total_seconds // (60*60)
total_seconds %= (60*60)

min = total_seconds // 60
total_seconds %= 60

print("Your estimated wait time is {} hour(s), {} minute(s), and {} second(s).".format(hour, min, total_seconds))