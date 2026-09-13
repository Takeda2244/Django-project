from dataclasses import dataclass
from typing import List, Optional, Dict

# Класс обычного допустим человека из которого будут наследовать учитель и студент
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
    
    # Определил метод info()

    def info(self) -> str:
        return f"Имя: {self.name}, возраст {self.age}"

# Класс Student который наследуется от Person
class Student(Person):
    def __init__(self, name: str, age: int, grades: List[int]) -> None:
        # Инициализация переменных родительского класса
        super().__init__(name, age)

        self.grades: List[int] = grades

    # Переопределение метода info() что опзволяет добавить новые данные к уже существующим
    def info(self) -> str:
        # Взяли метод родительского класса info() и добавили кроме возраста и имени оценки
        # Я для себя помечаю: super() позволяет наследовать переменные и методы род класса
        info_rod: str = super().info()
        return f"{info_rod}, оценки: {self.grades}"

# Делаю учителя через dataclass чтобы читабельнее код был
@dataclass
class Teacher:
    name: str
    age: int
    subjects: List[str]
    # Как я понял optional позволяет записать в переменную данные одного типа либо никакого
    classroom: Optional[int] = None

    # Реализация info() в дата классе а не обычном классе
    def info(self) -> str:
        return f"Имя преподователя: {self.name}, возраст: {self.age}, " \
        f"предметы которые ведет: {self.subjects}, класс в котором находится: {self.classroom}"

# Демонстрация работы
if __name__ == "__main__":
    student: Student = Student(name="Алексей", age=15, grades=[5, 4, 5])
    teacher: Teacher = Teacher(name="Артем Петров", age=45, subjects=["Python", "C++"], classroom=15)

# Создал бд с выводом о преподователе и студенте

# Работа полиморфизма метод info() с студентом и преподователем выведет разный текст
db: Dict[str, List[str]] = {
    "Студент": [student.info()],
    "Преподователь": [teacher.info()]
}

for group, members in db.items():
    print(f"{group}:")
    for member in members:
        print(member)