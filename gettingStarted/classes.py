students = []

class Student:

    schoolName = "Catherine Bell Elementary"

    def __init__(self, name, student_id=332):
        #student = {"name": name, "student_id": student_id}
        #students.append(student)
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return f"Student: {self.name}"

    def get_name_capitalize(self):
        return self.name.capitalize()
    
    def getSchoolName(self):
        return self.schoolName

cesar = Student("Cesar")

print(cesar)
print(cesar.get_name_capitalize())
print(cesar.getSchoolName())

#print class attribute (static)
print(Student.schoolName)

#print(students)
