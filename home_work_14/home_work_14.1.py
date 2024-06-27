class GroupLimitReachedException(Exception):
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.gender} {self.age}'

    def show_info(self):
        print(self.__str__())


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f' {self.record_book}'

    def show_info(self):
        print(f"Name: {self.first_name} has {self.record_book}")


class Group:

    def __init__(self, number, student_limit=10):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) == self.student_limit:
            raise GroupLimitReachedException(f"Group limit {self.student_limit} reached", self.number)
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__() + '\n'
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st4 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st5 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st7 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st8 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st9 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st10 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)

except GroupLimitReachedException as error:
    print(error)
except Exception as error:
    print(error)

print(gr)