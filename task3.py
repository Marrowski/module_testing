import unittest

class Student:
    def __init__(self, name: str, surname: str, age: int, avg_mark: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_mark = avg_mark


stud1 = Student('Oleh', 'Yemelianov', 21, 4.5)
stud2 = Student('Ivan', 'Petrov', 19, 3.2)
stud3 = Student('Dmytro', 'Sidorov', 20, 5.0)
stud4 = Student('Danylo', 'Ivanov', 24, 4.3)
stud5 = Student('Alex', 'Alexeev', 23, 2.5)
stud6 = Student('Oleksiy', 'Danylov', 18, 4.9)
stud7 = Student('Olexander', 'Matveev', 18, 2.7)
stud8 = Student('Vadym', 'Tytov', 18, 1.8)
stud9 = Student('Yehor', 'Petrov', 22, 4.6)
stud10 = Student('Yevhen', 'Davydenko', 21, 4.0)

class TestStudent(unittest.TestCase):
    def test_values(self):
        self.assertNotEqual(stud1, stud2), 'Not equal.'
        self.assertIsNone(stud7), 'Successfully not none.'
        self.assertGreater(stud8.age, 17)
        self.assertEqual(stud2.age, 21)
        self.assertEqual(stud1.age, stud3.age)