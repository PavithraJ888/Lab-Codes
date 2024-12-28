subjects = [
    "Data Structures", 
    "Object-Oriented Programming", 
    "Database Management Systems", 
    "Operating Systems", 
    "Python Programming Lab", 
    "Software Engineering", 
    "Computer Networks", 
    "Digital Logic Design"
]
print("Displaying the  list of subjects:")
for subject in subjects:
    print(subject)
print("\n2nd and 5th elements of the list:")
print("2nd Element:", subjects[1])  
print("5th Element:", subjects[4])
print("\nFirst 4 elements of the list:")
print(subjects[:4]) 
print("\nLast 4 elements of the list:")
print(subjects[-4:])  
print("\nChecking if 'Python Programming Lab' is in the list:")
if "Python Programming Lab" in subjects:
    print("Yes, 'Python Programming Lab' is in the list.")
else:
    print("No, 'Python Programming Lab' is not in the list.")
print("\nDemonstrating append() function:")
subjects.append("Machine Learning")   
print("Updated list after append:", subjects)
print("\nDemonstrating insert() function:")
subjects.insert(3, "Artificial Intelligence") 
print("Updated list after insert:", subjects) 
print("\nDemonstrating remove() function:")
subjects.remove("Database Management Systems")  
print("Updated list after remove:", subjects) 
print("\nDemonstrating pop() function:")
popped_subject = subjects.pop(2)  
print(f"Popped subject: {popped_subject}")
print("Updated list after pop:", subjects)
