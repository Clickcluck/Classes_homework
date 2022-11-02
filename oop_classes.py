class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in \
                self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_student_grade(self):
        result = []
        for value in self.grades.values():
            result += value
        return sum(result) / len(result)

    def __str__(self):
        student_info = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
                       f"Средняя оценка: {self._average_student_grade()}\n" \
                       f"Курсы в процессе изучения: " \
                       f"{''.join(self.courses_in_progress)}\n" \
                       f"Завершенные курсы: {''.join(self.finished_courses)}"
        return student_info


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_lecturer_grade(self):
        result = []
        for value in self.grades.values():
            result += value
        return sum(result) / len(result)

    def __str__(self):
        lecturer_info = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
                        f"Средняя оценка: {self._average_lecturer_grade()} "
        return lecturer_info

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self._average_lecturer_grade() < other._average_student_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = f"Имя: {self.name}\nФамилия: {self.surname}"
        return info


nicola_student = Student('Nicola', 'Tesla', 'male')
nicola_student.courses_in_progress += ['Physics']
nicola_student.finished_courses += ['Maths']

zenobe_lecturer = Lecturer('Zenobe', 'Gramme')
zenobe_lecturer.courses_attached += ['Physics']
nicola_student.rate_lectures(zenobe_lecturer, 'Physics', 10)
nicola_student.rate_lectures(zenobe_lecturer, 'Physics', 10)
nicola_student.rate_lectures(zenobe_lecturer, 'Physics', 10)
zenobe_lecturer._average_lecturer_grade()

thomas_reviewer = Reviewer('Tomas', 'Edison')
thomas_reviewer.courses_attached += ['Physics']
thomas_reviewer.courses_attached += ['Physics']

thomas_reviewer.rate_hw(nicola_student, 'Physics', 8)
thomas_reviewer.rate_hw(nicola_student, 'Physics', 8)
thomas_reviewer.rate_hw(nicola_student, 'Physics', 8)
nicola_student._average_student_grade()

print(nicola_student.__str__(), '\n')
print(zenobe_lecturer.__str__(), '\n')
print(thomas_reviewer.__str__())

print('\n', '*' * 60, '\n')

marie_student = Student('Marie', 'Curie', 'female')
marie_student.courses_in_progress += ['Physics']
marie_student.finished_courses += ['Chemistry']

gabriel_lecturer = Lecturer('Gabriel', 'Lippman')
gabriel_lecturer.courses_attached += ['Physics']
marie_student.rate_lectures(gabriel_lecturer, 'Physics', 10)
marie_student.rate_lectures(gabriel_lecturer, 'Physics', 10)
marie_student.rate_lectures(gabriel_lecturer, 'Physics', 10)
gabriel_lecturer._average_lecturer_grade()


henri_reviewer = Reviewer('Henri', 'Becquerel')
henri_reviewer.courses_attached += ['Physics']
henri_reviewer.rate_hw(marie_student, 'Physics', 10)
henri_reviewer.rate_hw(marie_student, 'Physics', 10)
henri_reviewer.rate_hw(marie_student, 'Physics', 10)
marie_student._average_student_grade()


print(marie_student.__str__(), '\n')
print(gabriel_lecturer.__str__(), '\n')
print(henri_reviewer.__str__())


students = [nicola_student, marie_student]
lecturers = [zenobe_lecturer, gabriel_lecturer]


def average_student_course_grade(students, course):
    combined_grades = []
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                combined_grades.append(value)
    result = [item for items in combined_grades for item in items]
    return sum(result) / len(result)


print(average_student_course_grade(students, 'Physics'))


def average_lecturer_course_grade(lecturers, course):
    combined_grades = []
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                combined_grades.append(value)
    result = [item for items in combined_grades for item in items]
    return sum(result) / len(result)

print(average_lecturer_course_grade(lecturers, 'Physics'))
