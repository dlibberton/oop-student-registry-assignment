class Student:
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = name
        self._age = age
        self._grade = grade
        
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 3 and ' ' not in new_name and not any(char in "!@#$%^&*()[]{};:,.<>?/|\\`~" for char in new_name) and new_name.istitle():
            self._name = new_name

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age
    
    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        if isinstance(new_grade, str) and new_grade in ["9th", "10th", "11th", "12th"]:
            self._grade = new_grade

    def __str__(self):
        return f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
Francisco = Student("Francisco", 15, "12th")

print(Francisco)