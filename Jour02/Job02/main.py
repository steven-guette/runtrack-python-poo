from classes.student import Student
from classes.teacher import Teacher

student = Student()
teacher = Teacher()

student.SetAge(15)
teacher.SetAge(40)

print("\nÉlève :")
student.SayHello()
student.GoToClass()

print("\nProfesseur :")
teacher.SayHello()
teacher.Teach()
