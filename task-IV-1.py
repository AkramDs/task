class Students:
    def total(self, first_name, last_name, year_of_entrance, department):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_entrance = year_of_entrance
        self.department = department

        total = f'{first_name.title()} {last_name.title()} поступил(а) в {year_of_entrance}г. Факультет: {department}.'

        return total

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
year_of_entrance = int(input('Введите год поступление: '))
department = input('Введите факультет: ')

student = Students()
print(student.total(first_name, last_name, year_of_entrance, department))
