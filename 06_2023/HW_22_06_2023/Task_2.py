import openpyxl

r1 = ["STUDENT'S NAME", 'COURSE', 'BRANCH', 'SEMESTER']
r2 = ['ANKIT RAI', 'B.TECH', 'CSE', 4]
r3 = ['RAHUL RAI', 'M.TECH', 'CSE', 2]
r4 = ['PRIYA RAI', 'MBA', 'HR', 3]
r5 = ['AISHWARYA', 'B.TECH', 'CSE', 4]
r6 = ['HARSHITA JAISWAL', 'B.TECH', 'BIOTECH', 5]
count = [r1, r2, r3, r4, r5, r6]

aw = openpyxl.Workbook()
b = aw.active
b.column_dimensions['A'].width = 30
for x in count:
    b.append(x)

aw.save('example.xlsx')
