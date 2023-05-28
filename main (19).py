class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def evaluation_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rating_student(self):
        if not self.grades:
            return 0
        grade = []
        for x in self.grades.values():
            grade.extend(x)
        return round(sum(grade)/len(grade), 2)
            

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.rating_student()}\nКурсы в процессе обучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'
        
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rating_lecturer(self):
        if not self.grades:
            return 0
        grade = []
        for x in self.grades.values():
            grade.extend(x)
        return round(sum(grade)/len(grade), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating_lecturer()}\n'

    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


def rating(persons, course):
    if not isinstance(persons, list):
        return "Not list"
    grades_persons = []
    for person in persons:
        grades_persons.extend(person.grades.get(course, []))
    if not grades_persons:
        return "По такому курсу нет ни у кого оценок"
    return round(sum(grades_persons)/len(grades_persons), 2)


 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)


student_sue = Student('Sue', 'Richman', 'female')
student_sue.courses_in_progress += ['C++']

cool_lecturer = Lecturer('Genry', 'Green')
cool_lecturer.courses_attached += ['C++']

student_sue.evaluation_lectures(cool_lecturer, 'C++', 10)

cool_reviewer = Reviewer('Harry', 'Potter')
cool_reviewer.courses_attached += ['C++']

cool_reviewer.rate_hw(student_sue, 'C++', 8)
cool_reviewer.rate_hw(student_sue, 'C++', 7)

student_angry = Student('Malfoy', 'Drago', 'male')
student_angry.courses_in_progress += ['C++']
student_angry.courses_in_progress += ['Python']
student_angry.finished_courses += ['Anger Managemen']

angry_reviewer = Reviewer('Severus', 'Snape')
angry_reviewer.courses_attached += ['C++']
angry_reviewer.courses_attached += ['Python']

angry_reviewer.rate_hw(student_angry, 'C++', 2)
angry_reviewer.rate_hw(student_angry, 'Python', 6)
angry_reviewer.rate_hw(student_sue, 'C++', 5)
angry_reviewer.rate_hw(best_student, 'Python', 5)

angry_lecturer = Lecturer('Sheev', 'Palpatine')
angry_lecturer.courses_attached += ['C++']
angry_lecturer.courses_attached += ['Python']

student_sue.evaluation_lectures(angry_lecturer, 'C++', 10)
student_sue.evaluation_lectures(angry_lecturer, 'C++', 9)
student_angry.evaluation_lectures(angry_lecturer, 'Python', 3)
student_angry.evaluation_lectures(angry_lecturer, 'C++', 4)
best_student.evaluation_lectures(angry_lecturer, 'Python', 6)
best_student.evaluation_lectures(angry_lecturer, 'Python', 7)

lecturer_tony = Lecturer('Tony', 'Stark')
lecturer_tony.courses_attached += ['C++']
lecturer_tony.courses_attached += ['Python']
lecturer_tony.courses_attached += ['Anger Managemen']

student_sue.evaluation_lectures(lecturer_tony, 'C++', 10)
student_sue.evaluation_lectures(lecturer_tony, 'C++', 9)
student_angry.evaluation_lectures(lecturer_tony, 'Python', 9)
student_angry.evaluation_lectures(lecturer_tony, 'C++', 8)
best_student.evaluation_lectures(lecturer_tony, 'Python', 9)
best_student.evaluation_lectures(lecturer_tony, 'Python', 8)

halk_reviewer = Reviewer('Bruce', 'Banner')
halk_reviewer.courses_attached += ['C++']
halk_reviewer.courses_attached += ['Python']
halk_reviewer.courses_attached += ['Anger Managemen']

halk_reviewer.rate_hw(student_sue, 'C++', 9)
halk_reviewer.rate_hw(student_angry, 'C++', 9)
halk_reviewer.rate_hw(student_angry, 'Python', 9)
halk_reviewer.rate_hw(student_sue, 'C++', 9)
halk_reviewer.rate_hw(best_student, 'Python', 9)
halk_reviewer.rate_hw(student_sue, 'C++', 9)


student_list = [best_student, student_angry, student_sue]
lecturer_list = [lecturer_tony, angry_lecturer, cool_lecturer]


print("Средняя оценка студентов по С++: "+ str(rating(student_list, 'C++')))
print("Средняя оценка студентов по Python: " + str(rating(student_list, 'Python')))
print("Средняя оценка за лекции у преподавателей по Python: " + str(rating(lecturer_list, 'Python')))
print("Средняя оценка за лекции у преподавателей по C++: " + str(rating(lecturer_list, 'C++')))
print(lecturer_tony)
        