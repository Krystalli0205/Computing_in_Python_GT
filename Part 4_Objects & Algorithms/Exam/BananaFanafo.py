#Write a function called bananafy. bananafy should take one
#parameter, a string. bananafy should replace every vowel in
#the string with the previous vowel from the alphabet: e should
#become a, i should become e, o should become i, and u should
#become o. a should, in turn, become u. This should be done
#for both capital and lower-case vowels. Then, bananafy should
#return the result.
#
#For example:
#
# bananafy("banana") -> "bununu"
# bananafy("benene") -> "banana"
# bananafy("AEIOU") -> "UAEIO"
# bananafy("Four Score And Seven Years") -> "Fior Scira Und Savan Yaurs"

#Write your function here!
def bananafy(a_string):
    vowel = {"a":"u", "e":"a", "i":"e", "o":"i", "u":"o",
              "A": "U", "E": "A", "I": "E", "O": "I", "U": "O"}

    res = ""

    for char in a_string:
        if char in vowel:
            res += vowel[char]
        else:
            res += char

    return res


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the same results as in the examples above.
print(bananafy("banana"))
print(bananafy("benene"))
print(bananafy("AEIOU"))
print(bananafy("Four Score And Seven Years"))


