import json
#All students object will be stored in this dictionary
students = {}
#All course objects will reside here
courses = {}

class Person:
	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address
	def display_person_info(self):
		print(f"Person Name: {name}")
		print(f"Person Age: {age}")
		print(f"Person Address: {address}")

class Student(Person):
	def __init__(self, name, age, address, student_id):
		super().__init__(name, age, address)
		self.student_id = student_id
		self.grades = {}
		self.courses = []
	
	def add_grade(self, subject, grade):
		self.grades[subject] = grade

	def enroll_course(self, course):
		self.courses.append(course)

	def display_student_info(self):
		print()
		print(f"Student Id: {self.student_id}")
		print(f"Student's Name: {self.name}")
		print(f"Student's Age: {self.age}")
		print(f"Student's Address: {self.address}")
		print("Student's Subjects and Grades: ")
		for key in self.grades:
			print(f"{key}: {self.grades[key]}")
		print()
		print("Student's Enrolled Courses:")
		for course in self.courses:
			print(f"** {course}")

class Course:
	def __init__(self, course_name, course_code, instructor):
		self.course_name = course_name
		self.course_code = course_code
		self.instructor = instructor
		self.students = []
	
	def add_student(self, student):
		self.students.append(student)
	
	def display_course_info(self):
		print(f"Course Code: {self.course_code}")
		print(f"Course Name: {self.course_name}")
		print(f"Course Instructor: {self.instructor}")
		print("Students Enrolled in this course: ")
		for student in self.students:
			print(f"{student}")

#user prompts
while True:
	print()
	print("==== Student Management System ====")
	print()
	print("1. Add New Student")
	print("2. Add New Course")
	print("3. Enroll Student in Course")
	print("4. Add Grade for Student")
	print("5. Display Student Details")
	print("6. Display Course Details")
	print("7. Save Data to File")
	print("8. Load Data from File")
	print("0. Exit")
	print()
	option = int(input("Select Option: "))
	print()
	if option < 0 or option > 8:
		print("Invalid Option!")
		print()
		continue

	if option == 1:
		name = input("Enter Name: ")
		age = int(input("Enter Age: "))
		address = input("Enter Address: ")
		student_id = input("Enter Student Id: ")
		if student_id in students.keys():
			print("Student Id Already Exists!")
			print()
			continue
		students[student_id] = Student(name, age, address, student_id)
		print()
		print(f"Student: {students[student_id].name} (ID: {students[student_id].student_id}) added successfully.")
		print()
	elif option == 2:
		name = input("Enter Course Name: ")
		course_code = input("Enter Course Code: ")
		if course_code in courses.keys():
			print("Course Code already exists!")
			print()
			continue
		instructor = input("Enter Instructor Name: ")
		courses[course_code] = Course(name, course_code, instructor)
		print()
		print(f"Course: {courses[course_code].course_name} (Code: {courses[course_code].course_code}) created with instructor {courses[course_code].instructor}")
		print()
	elif option == 3:
		student_id = input("Enter Student Id: ")
		course_code = input("Enter Course Code: ")
		print()
		if student_id in students.keys():
			if course_code in courses.keys():
				students[student_id].courses.append(courses[course_code].course_name)
				courses[course_code].students.append(students[student_id].name)
				print(f"Student {students[student_id].name} (ID: {student_id}) endrolled in {courses[course_code].course_name} (Code: {course_code}).")
			else:
				print("Invalid Syntax!")
		else:
			print("Invalid Student!")
	elif option == 4:
		student_id = input("Enter Student Id: ")
		course_code = input("Enter Course Code: ")
		grade = input("Enter Grade: ")
		print()
		if student_id in students.keys():
			if course_code in courses.keys():
				if courses[course_code].course_name in students[student_id].courses:
					students[student_id].grades[courses[course_code].course_name] = grade
					print(f"Grade {grade} added for {students[student_id].name} in {courses[course_code].course_name}")
				else:
					print("Student is not enrolled in this course!")
			else:
				print("Invalid Course!")
		else:
			print("Invalid Student!")
	elif option == 5:
		student_id = input("Enter Student Id: ")
		print()
		if student_id in students.keys():
			students[student_id].display_student_info()
		else:
			print("Invalid Student Id!")
	elif option == 6:
		course_code = input("Enter course code: ")
		print()
		if course_code in courses.keys():
			print("Course Information: ")
			courses[course_code].display_course_info()
		else:
			print("Invalid Course Code!")
	elif option == 7:
		#creating a dictionary and filling it with all student data to convert that dict to json
		students_python_dict = {}
		i = 1
		for st in students:
			students_python_dict[f"Student {i}"] = {}
			students_python_dict[f"Student {i}"]["Student Id"] = students[st].student_id
			students_python_dict[f"Student {i}"]["Student Name"] = students[st].name
			students_python_dict[f"Student {i}"]["Age"] = students[st].age
			students_python_dict[f"Student {i}"]["Address"] = students[st].address
			students_python_dict[f"Student {i}"]["Grades"] = students[st].grades
			students_python_dict[f"Student {i}"]["Courses"] = students[st].courses
			i += 1

		courses_python_dict = {}
		i = 1
		for course in courses:
			courses_python_dict[f"Course {i}"] = {}
			courses_python_dict[f"Course {i}"]["Course Code"] = courses[course].course_code
			courses_python_dict[f"Course {i}"]["Course Name"] = courses[course].course_name
			courses_python_dict[f"Course {i}"]["Course Instructor"] = courses[course].instructor
			courses_python_dict[f"Course {i}"]["Enrolled Students"] = courses[course].students
			i += 1

		all_data_dict = {}
		all_data_dict["students"] = students_python_dict
		all_data_dict["courses"] = courses_python_dict
		json_data = json.dumps(all_data_dict, indent=4)
		
		with open("all_data.json", "w") as file:
			file.write(json_data)

		print("All data saved to file Successfully!")
		print()
	
	elif option == 8:
		retrieved_data = ""
		with open("all_data.json", "r") as file:
			retrieved_data = file.read()
		loaded_data = json.loads(retrieved_data)
		print("Data loaded from file successfully!")
		print()


	elif option == 0:
		print("Exiting Student Management System. Goodbye!")
		print()
		break
