from student import *

class HighSchoolStudent(Student):
    """
    HighSchoolStudent Class
    """

    schoolName = "Rodriguez High School"

    def get_name_capitalize(self):
        return super().get_name_capitalize() + "-HS"


