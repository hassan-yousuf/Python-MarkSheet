# Getting User Name
studentName = str(input('Name: '))
studentFatherName = str(input('Father Name: '))

# Getting User Marks
urduMarks = int(input('Urdu: '))
mathMarks = int(input('Math: '))
englishMarks = int(input('English: '))
sindhiMarks = int(input('Sindhi: '))
biologyMarks = int(input('Biology: '))
islamiatMarks = int(input('Islamiat: '))
chemistryMarks = int(input('Chemistry: '))
physicsMarks = int(input('Physics: '))
pakistanStudiesMarks = int(input('Pakistan Studies: '))
obtainedMarks = (urduMarks + mathMarks + englishMarks + sindhiMarks + biologyMarks + islamiatMarks + chemistryMarks + physicsMarks + pakistanStudiesMarks)
totalMarks = 900
percentage = (obtainedMarks / totalMarks * 100)
# Displaying User Percentage
print(studentName + ' ' + studentFatherName + ' got ' + str(format(percentage, '.0f')) + '%')