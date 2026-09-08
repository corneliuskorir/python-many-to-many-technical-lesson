class Student:
    all = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Student.all.append(self)

    def courses(self):
        return [
            schedule.course for schedule in Schedule.all if schedule.student == self
        ]

    def calculate_gpa(self):
        grades = [
            scheduel.grade for scheduel in Schedule.all if scheduel.student == self
        ]

        return sum(grades) / len(grades)


class Course:
    all = []

    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        Course.all.append(self)

    def students(self):
        return [
            schedule.student for schedule in Schedule.all if schedule.course == self
        ]


class Schedule:
    all = []

    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
        Schedule.all.append(self)

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, value):
        if not isinstance(value, Student):
            raise Exception
        self._student = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if not isinstance(value, Course):
            raise Exception
        self._course = value
