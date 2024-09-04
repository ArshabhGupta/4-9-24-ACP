class dogs:
    species = 'dog'
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

Charlie = dogs("Charlie" ,10 ,"Border Collie")
Milo = dogs("Milo",15 ,"Golden Retriever")

print("{} is a {} and is {} years old".format(Charlie.name, Charlie.age, Charlie.breed))
print("{} is a {} and is {} years old".format(Milo.name, Milo.age, Milo.breed))    