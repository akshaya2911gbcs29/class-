class Student:
    def process_student_data(self):
        self.name = input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        print("Enter marks for 5 subjects (out of 100):")
        self.marks = []
        for i in range(5):
            mark = float(input(f"  Subject {i + 1} marks: "))
            self.marks.append(mark)
        self.total = sum(self.marks)
        self.average = self.total / 5.0
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Total Marks: {self.total}")
        print(f"Average Marks: {self.average:.2f}")
        print(f"Grade: {self.grade}")
student1 = Student()
student1.process_student_data()
