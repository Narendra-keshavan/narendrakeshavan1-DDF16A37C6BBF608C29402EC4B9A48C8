class Student:  
    def _init_(self, name, roll_number, cgpa): 
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa 

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students = [ 
    Student("narendrakeshavan", "2222k0150", 9.8),
    Student("keshav", "222k0142", 9.7),
    Student("naren", "2222k0156", 8.0),
    Student("Nk", "2222k0152", 9.0)  
]
sorted_students = sort_students(students)

for student in sorted_students:
    print("Name: {}, Roll_number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))