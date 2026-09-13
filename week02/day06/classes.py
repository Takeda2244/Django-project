# Класс студента
class Student:
    def __init__(self, name, age, grades_student):
        self.name = name
        self.age = int(age)
        self.grades = [float(grades_student)]

    # Добавление оценки в оценки студента
    def add_grade(self, grade):
        if 1 <= float(grade) <= 5:
            self.grades.append(float(grade))
        else:
            raise ValueError("Оценка должна быть в диапазоне от 1 до 5")
        
    # Вывод среднего балла студента
    def average(self):
        if not self.grades:
            print("У студента ещё нет отценок")
        else:
            average_grade = round(sum(self.grades) / len(self.grades), 2)
            return average_grade

    # Вывести данные о студенте в словарь
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grades": self.grades, 
            "average_grade": self.average()
        }

# Класс группы
class Group:
    def __init__(self, group):
        self.group = group
        self.students = []

    # Добавить студента в группу
    def add(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    # Удалить группу из списка групп
    def delete(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                return True
        return False

    # Найти студента в группе
    def find(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student
        return None
    
    # Вывести 5 лучших студентов
    def top_students(self):
        def student_average(student):
            return student.average()

        sorted_students = sorted(self.students, key=student_average, reverse=True)
        
        return sorted_students[:5]