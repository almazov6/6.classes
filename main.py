class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_rating(self):
        if len(self.grades) != 0:
            return sum([int(i) for i in self.grades.values()]) / len(self.grades.values())
        else:
            return 'Нет оценок'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._average_rating()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __eq__(self, other):
        return self._average_rating() == other._average_rating()

    def __ne__(self, other):
        return self._average_rating() != other._average_rating()

    def __lt__(self, other):
        return self._average_rating() < other._average_rating()

    def __le__(self, other):
        return self._average_rating() <= other._average_rating()

    def __gt__(self, other):
        return self._average_rating() > other._average_rating()

    def __ge__(self, other):
        return self._average_rating() >= other._average_rating()

    def course_evaluation(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            return 'Ошибка'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __eq__(self, other):
        return self._average_rating() == other._average_rating()

    def __ne__(self, other):
        return self._average_rating() != other._average_rating()

    def __lt__(self, other):
        return self._average_rating() < other._average_rating()

    def __le__(self, other):
        return self._average_rating() <= other._average_rating()

    def __gt__(self, other):
        return self._average_rating() > other._average_rating()

    def __ge__(self, other):
        return self._average_rating() >= other._average_rating()

    def _average_rating(self):
        if len(self.grades) != 0:
            return sum([int(i) for i in self.grades.values()]) / len(self.grades.values())
        else:
            return 'Нет оценок'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating()}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

lectur1 = Lecturer('Max', 'Gigo')
lectur1.courses_attached += ['Python', 'Git']

lectur2 = Lecturer('Rezeda', 'Almazova')
lectur2.courses_attached += ['Python', 'Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python', 'Git']
best_student.course_evaluation(lectur1, 'Python', '10')
best_student.course_evaluation(lectur1, 'Git', '7')

best_student1 = Student('Rezeda', 'Almazova', 'your_gender')
best_student1.finished_courses += ['Введение в программирование']
best_student1.courses_in_progress += ['Python', 'Git']
best_student1.course_evaluation(lectur2, 'Python', '5')
best_student1.course_evaluation(lectur2, 'Git', '7')


reviewer1 = Reviewer('Some', 'Didikal')
reviewer1.courses_attached += ['Python', 'Git']
reviewer1.rate_hw(best_student, 'Python', '6')
reviewer1.rate_hw(best_student, 'Git', '3')
reviewer1.rate_hw(best_student1, 'Python', '6')
reviewer1.rate_hw(best_student1, 'Git', '3')

