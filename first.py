
students=[]
while input("press 1 to continue any ket to exit....")=='1':
	name=input('Please enter the name')
	age=int(input('Please enter the age'))
	contactNumber=input('Please enter the contact')
	students.append([name,age,contactNumber])

file=open("d:\\Studentss.txt","w")
file.writeLine(students[0][0],students[0][1],,students[0][2])

for student in students:
	print("Name : {0} \nAge : {1} \ncontactNumber: {2}".format(student[0],student[1],student[2]))





