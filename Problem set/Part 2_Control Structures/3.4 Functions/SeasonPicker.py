#Write a function called what_season. what_season should
#have two parameters: the first a string representing
#a month, and the second an integer representing a day.
#
#what_season should return "Spring" if the date is in
#Spring, "Summer" if it's in Summer, "Fall" if it's in
#Fall, and "Winter" if it's in Winter.
#
#For this problem, we define those seasons as follows:
#
# - Spring starts March 20.
# - Summer starts June 21.
# - Fall starts September 22.
# - Winter starts December 21.
#
#So, March 20 to June 20 would be Spring; June 21 to
#September 21 would be Summer; September 22 to December
#20 would be Fall; and December 21 to March 19 would be
#Winter.


#Add your code here!
def what_season(mth, day):
    if mth in ["April", "May"] or mth == "March" and day >= 20 or mth == "June" and day < 21:
        return "Spring"
    elif mth in ["July", "August"] or mth == "June" and day >= 21 or mth == "September" and day < 22:
        return "Summer"
    elif mth in ["October", "November"] or mth == "September" and day >= 22 or mth == "December" and day < 21:
        return "Fall"
    elif mth in ["January", "February"] or mth == "December" and day >= 21 or mth == "March" and day < 20:
        return "Winter"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print Winter, Spring, Summer, and Fall in that order.
print(what_season("December", 25))
print(what_season("June", 15))
print(what_season("June", 23))
print(what_season("September", 27))

