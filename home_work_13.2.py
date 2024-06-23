'''
Створити клас цифрового лічильника. У класі реалізувати методи:
встановлення максимального значення лічильника,
встановлення мінімального значення лічильника
встановлення початкового значення лічильника
метод step_up збільшує лічильник на 1. Метод можна викликати до тих пір, поки значення досягне максимуму.
При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимумуʼ
метод step_down зменшує лічильник на 1. Метод можна викликати до тих пір, поки значення не досягне мінімуму.
При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що досягнутий мінімум
повернення поточного значення лічильника
Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод ініціалізації
екземпляра класу.'''


class Counter:

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       if start < self.min_value or start > self.max_value:
           raise ValueError(f"Current value must be between {self.min_value} and {self.max_value}.")
       self.current = start

   def set_max(self, max_value):
       if max_value < self.min_value:
           raise ValueError("Max value must be greater than or equal to min value.")
       self.max_value = max_value
       if self.current > max_value:
           self.current = max_value

   def set_min(self, min_value):
       if min_value > self.max_value:
           raise ValueError("Min value must be less than or equal to max value.")
       self.min_value = min_value
       if self.current < min_value:
           self.current = min_value

   def step_up(self):
       if self.current >= self.max_value:
           raise ValueError("Reached maximum value.")
       self.current += 1

   def step_down(self):
       if self.current <= self.min_value:
           raise ValueError("Reached minimum value.")
       self.current -= 1

   def get_current(self):
       return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
