
class Chef:

   def __init__(self, name, age):
       self.name = name
       self.age = age


   def make_chicken(self):
       print("The chef makes chicken")

   def make_salad(self):
       print("The chef makes salad")

   def make_special_dish(self):
       print("The chef makes bbq ribs")

class ItalianChef(Chef):

   def __init__(self, name, age, countryOfOrigin):
       self.countryOfOrigin = countryOfOrigin
       super().__init__(name, age)

   def make_pasta(self):
       print("The chef makes pasta")

   def make_special_dish(self):
       print("The chef makes chicken parm")


myChef = Chef("Gordon Ramsay", 50)
myChef.make_chicken()

myItalianChef = ItalianChef("Massimo Bottura", 55, "Italy")
myItalianChef.make_chicken()
print(myItalianChef.age);
