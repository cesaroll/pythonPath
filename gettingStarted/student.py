class Student:
    """
    Student Class
    """

    schoolName = "Catherine Bell Elementary"

    def __init__(self, name, student_id=332):
        
        self.name = name
        self.student_id = student_id
        

    def __str__(self):
        return "Student: {0}".format(self.name)

    def get_name_capitalize(self):
        return self.name.capitalize()
    
    def getSchoolName(self):
        return self.schoolName
