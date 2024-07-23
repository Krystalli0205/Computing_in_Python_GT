cafe = "Octane"
balance = 7.5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Atlanta is full of great coffee places. Unfortunately, great
#coffee is usually expensive. The variables above will
#contain a balance and a cafe name. Below are the prices of
#a cup of coffee at each of three locations:
#
# - Octane: $6
# - Galloway: $5
# - Starbucks: $4
# - Revelator: $3
# - Dunkin: $2
#
#Add some code above that will print one of the following
#two messages depending on whether the value of balance is
#high enough to buy a cup of coffee at the given cafe.
#
# - If it is sufficient, print "With [balance] dollars, I
#   can buy coffee at [cafe]"
# - If it is not sufficient, print "With [balance] dollars,
#   I cannot buy coffee at [cafe]"

#Add your code here!
con1 = cafe == "Octane" and balance >= 6
con2 = cafe == "Galloway" and balance >= 5
con3 = cafe == "Starbucks" and balance >= 4
con4 = cafe == "Revelator" and balance >= 3
con5 = cafe == "Dunkin" and balance >= 2



if con1 or con2 or con3 or con4 or con5:
    print("With {} dollars, I can buy coffee at {}".format(balance, cafe))
else:
    print("With {} dollars, I cannot buy coffee at {}".format(balance, cafe))


