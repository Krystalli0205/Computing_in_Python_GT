#Copy your Burrito class from the last exercise. Below,
#We've given you three additional classes named "Meat",  
#"Rice" and "Beans." We've gone ahead and built getters
#and setters in these classes to check if the incoming
#values are valid, so you'll be able to remove those
#from your original code.
#
#First, edit the constructor of your Burrito class.
#Instead of calling setters to set the values of the
#attributes self.meat, self.rice, and self.beans, it
#should instead create new instances of Meat, Rice, and
#Beans. The arguments to these new instances should be
#the same as the arguments you were sending to the
#setters previously (e.g. self.rice = Rice("brown")
#instead of set_rice("brown")).
#
#Second, modify your getters and setters from your
#original code so that they still return the same value
#as before. get_rice(), for example, should still
#return "brown" for brown rice, False for no rice, etc.
#instead of returning the instance of Rice.
#
#Third, make sure that your get_cost function still
#works when you're done changing your code.
#
#Hint: When you're done, creating a new instance of
#Burrito with Burrito("pork", True, "brown", "pinto")
#should still work to create a new Burrito. The only
#thing changing is the internal reasoning of the
#Burrito class.
#
#Hint 2: Notice that the classes Meat, Beans, and Rice
#already contain the code to validate whether input is
#valid. So, your setters in the Burrito class no
#longer need to worry about that -- they can just pass
#their input to the set_value() methods for those
#classes.
#
#Hint 3: This exercise requires very little actual
#coding: you'll only write nine lines of new code, and
#those nine lines all replace existing lines of code
#in the constructor, getters, and setters of Burrito.
#
#You should not need to modify the code below.

class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False
            

            
#Add and modify your code here!

class Burrito:

    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        self.meat = Meat(meat)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_to_go(to_go)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    valid_meat = ["chicken", "pork", "steak", "tofu", False]
    valid_rice = ["brown", "white", False]
    valid_beans = ["black", "pinto", False]

    

    def get_meat(self):
        return self.meat.get_value()
    
    def set_meat(self, new_meat):
        self.meat.set_value(new_meat)

    def get_to_go(self):
        return self.to_go
    
    def set_to_go(self, new_to_go):
        if isinstance(new_to_go, bool):
            self.to_go = new_to_go
        else:
            self.to_go = False
    
    def get_rice(self):
        return self.rice.get_value()

    def set_rice(self, new_rice):
        self.rice.get_value(new_rice)

    def get_beans(self):
        return self.beans.get_value()

    def set_beans(self, new_beans):
        self.beans.set_value(new_beans)
    
    def get_extra_meat(self):
        return self.extra_meat

    def set_extra_meat(self, new_meat):
        if isinstance(new_meat, bool):
            self.extra_meat = new_meat
        else:
            self.extra_meat = False

    def get_guacamole(self):
        return self.guacamole

    def set_guacamole(self, new_guac):
        if isinstance(new_guac, bool):
            self.guacamole = new_guac
        else:
            self.guacamole = False

    def get_cheese(self):
        return self.cheese

    def set_cheese(self, new_cheese):
        if isinstance(new_cheese, bool):
            self.cheese = new_cheese
        else:
            self.cheese = False

    def get_pico(self):
        return self.pico

    def set_pico(self, new_pico):
        if isinstance(new_pico, bool):
            self.pico = new_pico
        else:
            self.pico = False

    def get_corn(self):
        return self.corn

    def set_corn(self, new_corn):
        if isinstance(new_corn, bool):
            self.corn = new_corn
        else:
            self.corn = False

    def get_cost(self):
        base_cost = 5
        meat_val = self.get_meat()
        if meat_val in ["chicken", "pork", "tofu"]:
            base_cost += 1
        elif meat_val == "steak":
            base_cost += 1.5
        if self.get_extra_meat() and meat_val != False:
            base_cost += 1
        if self.get_guacamole():
            base_cost += 0.75
        return float(base_cost)

#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs. Remember though, the results
#of this code should be the same as the previous problem:
#what should be different is how it works behind the scenes.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("chicken", False, "brown", "black", extra_meat = "galactic", guacamole = False, cheese = False, pico = False, corn = False)
print(a_burrito.get_cost())

