class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('talk')


person = Person('John')

print(person.name)
