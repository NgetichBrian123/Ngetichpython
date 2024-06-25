
COURSES =["MIT","Cybersecurity","Datascience"]
print(COURSES)

#Adding a new element in an array
COURSES.append("Python")
print(COURSES)

#Removing an element in array
COURSES.remove("Datascience")

# Accessing an element in array
print(COURSES[1])

#Looping an array
for course in COURSES:
    print(course)