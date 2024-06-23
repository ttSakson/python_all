'''
Реалізуйте методи додавання,видалення студента та метод пошуку студента на прізвище.
Метод пошуку студента повинен повертати саме екземпляр класу Студент,
якщо студент є у групі, інакше - None.
У методі видалення, використовуйте результат методу пошуку.
Тобто. потрібно скомбінувати ці два методи;)
Визначте для групи метод str() для повернення списку студентів у вигляді рядка.


клас - це шаблон.
методи класу - це функції, які ми можемо виконувати всередині цього класу над його об'єктами.
Об'єкти класу - це екземпляри класу, його елементи, з яким ми працюємо (наприклад є клас студентів і ми в клас добалвяємо новий об'єкт, нового студента)
атрибути класу - це наче маркування об'єкта, щоб його описати, наприклад номер телефон студента є атрибутом.
__init__ - це метод (або функція у класі) що має назву "конструктор". він викликається коли ми створюємо новий об'єкт у класі і даємо йому початкові атрибути.
self - посилання для створення доступ до атрибутів в базовому класі.

'''


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}, Age: {self.age}, First Name: {self.first_name}, Last Name: {self.last_name}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group(Student):
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                return True
        return False

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Number:{self.number}\\n {all_students} "





st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
