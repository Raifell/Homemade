import openpyxl
from openpyxl.styles import Alignment, Font, Side, Border

r1 = ['', 'a', 'b', 'c']
r2 = ['one', 11, 21, 31]
r3 = ['two', 12, 22, 32]
r4 = ['three', 31, 32, 33]
count = [r1, r2, r3, r4]

aw = openpyxl.Workbook()
b = aw.active
for x in count:
    b.append(x)

for x in range(1, len(r1) + 1):
    for z in range(len(count)):
        if x == 1:
            b[x][z].alignment = Alignment(horizontal='center')
            b[x][z].font = Font(size=12, bold=True)
            cell = b[x][z]
            tolt = Side(border_style="medium")
            cell.border = Border(bottom=tolt, left=tolt, right=tolt)
        else:
            b[x][0].alignment = Alignment(horizontal='center')
            b[x][0].font = Font(size=12, bold=True)
            cell = b[x][0]
            tolt = Side(border_style="medium")
            cell.border = Border(top=tolt, bottom=tolt, right=tolt)

aw.save('example.xlsx')
