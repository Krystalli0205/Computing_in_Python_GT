bottle_month = "Feb"
bottle_day = 5
bottle_year = 21
use_by_month = "March"
use_by_day = 6
use_by_year = 21

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The lines above give the information for the bottle date and
#use by date for a bottle of salad dressing.
#
#Write some code that will generate what should be printed on
#the bottle. You should print two lines. The first line should
#be the bottle date itself, according to the following structure:
#
#Bottled Feb521
#
#Feb, 5, and 21 should be replaced by the values of bottle_month,
#bottle_day, and bottle_year, respectively.

#The second line should be the use by date, printed in more
#natural language, according to the following structure:
#
#For best experience, please use by March 6 2021.
#
#March, 6, and 21 should be replaced by the values of use_by_month,
#use_by_day, and use_by_year respectively. Note that you will need
#to add the '20' to the year; only the last two digits of the year
#are contained in use_by_year. Don't forget the period.


#Add your code here!
bottled_date = bottle_month + str(bottle_day) + str(bottle_year)
use_by_date = use_by_month + " " + str(use_by_day) + " 20" + str(use_by_year)

print("Bottled {}".format(bottled_date))
print("For best experience, please use by {}.".format(use_by_date))