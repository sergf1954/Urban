class Human:
    name = 'Петр'
    age  = 25
    pol  = 'м'
    def __init__(self,name,age,pol):
        self.name = name
        self.age  = age
        self.pol  = pol
        self.say_info()

    def __add__(self, other):
        sum_1 = self.age + other.age
        self.age = sum_1
        return self

    def __str__(self):
        return (f'Привет {self.name} Мне  {self.age} я {self.pol}')

    def say_info(self):
        print ( f'Привет {self.name} Мне  {self.age} я {self.pol} zzzzzzzzzzzzzzzzz')

    def birtday(self):
        self.age += 1
        return (f'{self.name} мой возраст {self.age} а было {self.age-1}')
    def __del__(self):
        pass
        #print(F'{self.name} Ушел ')

den = Human('Первый Den', 24, 'M')
print(den, id(den))
max = Human('Второй Max', 25, 'F')
print(max, id(max), 'До увеличения возраста')
den.surname = 'Попов'
print(den.name, den.surname)

den = den + max
print(den, id(den))
#print(den.name, max.name)
#print(den)
#del den

max.birtday()
print(max, id(max), 'После увеличения возраста ')
#den.birtday()

#max.say_info()

