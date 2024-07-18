class Student:
    def __init__(self,name,course):
       self.name=name
       self.course=course
    def details(self):
        print("----------Fees Details-----------")
        print(f"{'Name:':<20} {self.name:>10} \n{'course:':<20} {self.course:>10}")

class AccountOffice(Student):
    def __init__(self,name,course):
       super().__init__(name,course)
       super().details()
       
    def Calculation(self):
         found=False
         for department_courses in Courses:
            for department, courses in department_courses.items():
                for course_details in courses:
                    if course_details["course"].lower() == self.course.lower():
                        found=True
                        installments=["6 months","year"]
                        stud=input("student wants to pay for 6 months or year:")
                        if (stud.lower()==installments[0].lower()):
                           amt=course_details["fees"]/6
                           print(f"fees for 6 months: {amt}")
                        elif(stud.lower()==installments[1].lower()):
                           amt=course_details["fees"]/3
                           print(f"fees for 1 year: {amt}")  
                        amount=float(input("amount paid : "))
                        amount_due =amt-amount
                        if amount_due>0:
                             print(f"Amount Due: {amount_due:>.2f}")
                        else:
                             print("Successfully paid!")
         if not found:
            print("Course is not available")

Courses=[{"computer Science":[{"course":"bca","fees":450000,"Duration":3},{"course":"bsc(it)","fees":400000,"Duration":3},{"course":"bvoc","fees":390000,"Duration":3}]},
      {"Medical":[{"course":"bsc(medical)","fees":350000,"Duration":3},{"course":"bsc(biotechnology)","fees":370000,"Duration":3}]}
      ]
for department_courses in Courses:
    for department, courses in department_courses.items():
        print(f"Department: {department}")
        print("Courses:")
        for course_details in courses:
            print(f"- Course: {course_details["course"]}\n\t Fees: {course_details["fees"]}")
        print() 
print("----------student details-----------")
Name=input("enter a name: ")
Course=input("Course:")
info=AccountOffice(Name,Course)
info.Calculation()