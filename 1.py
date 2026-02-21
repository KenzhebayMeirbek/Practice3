class Person:
    def __init__(self, name , surname , age):
        self.name = name
        self.age = age
        self.surname = surname

    def show(self):
        print(f"Full name: {self.name} {self.surname}, Age: {self.age}.")



class Student(Person):
    def __init__(self , name, surname, age, id , gpa):
        super().__init__(name, surname, age)
        self.gpa = gpa
        self.id = id

    def show(self):
        
        print(f"Full name:{super(self.name)} {super(self.surname)} , Age: {super(self.age)} , GPA: {self.gpa}, ID: {self.id}")


a = input().split()
person1 = Student( a[0] , a[1] , a[2] , a[3] , a[4])
person1.show()
