""" This module defines a Student class to manage student grades and their average. """

class Student:
    ''' Class to represent a student with grades and methods to manage them '''

    next_id = 0

    def __init__(self, name):
        '''
        Initialize the student with an ID and name
        :param id: Student ID
        :param name: Student name
        :type id: str
        '''
        self.id = str(Student.next_id)
        self.next_id += 1
        self.name = name
        self.grades = []
        self.letter = ""
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, g):
        ''' Add a grade to the student's list of grades '''
        if isinstance(g, (int, float)) and 0 <= g <= 100:
            self.grades.append(g)
        else:
            print(f"Error: La calificación '{g}' no es válida. Debe ser un número entre 0 y 100.")

    def calc_average(self):
        ''' Calculate the average of grades '''
        if not self.grades:
            print("No hay calificaciones para calcular el promedio.")
            return 0
        t = sum(self.grades)
        avg = t / len(self.grades)
        return avg

    def avg_grade_to_letter(self):
        ''' Convert average grade to letter grade '''
        avg = self.calc_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"


    def delete_grade(self, index):
        ''' Delete a grade by index '''
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Error: Índice {index} fuera de rango. No se puede eliminar la calificación.")

    def check_honor(self):
        ''' Check if the student is eligible for honors '''
        self.honor = self.calc_average() >= 90

    def check_passed(self):
        ''' Check if the student has passed '''
        avg = self.calc_average()
        if avg >= 60:
            self.is_passed = "YES"
        else:
            self.is_passed = "NO"
        return self.is_passed

    def report(self):
        ''' Print a report of the student's information '''
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + self.avg_grade_to_letter())
        print("Average: " + str(self.calc_average()))
        print("Passed: " + self.check_passed())
        print("Honor Roll: " + ("Yes" if self.honor else "No"))


def startrun():
    ''' Function to run the student grade management '''
    a = Student("x")
    a.add_grades(100)
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()

startrun()
