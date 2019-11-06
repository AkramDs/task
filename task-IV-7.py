class Student:
    def __init__(self, full_name, age, major):
        self.full_name = full_name
        self.age = age
        self.major = major

    def __str__(self):
        return f'<name: {self.full_name}, age: {self.age}, major: {self.major}>'
        

steve = Student('Akram Dshakipov', 16, 'Programmer')
print(steve)
