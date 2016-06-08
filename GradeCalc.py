A = 0
B = 0
C = 0
D = 0
F = 0

i1 = input("Enter Student Grades (enter Z to indicate your list is finished):").upper()
while i1 != 'Z':
       if i1 == 'A':
              A = A + 1
       elif i1 == 'B':
              B = B + 1
       elif i1 == 'C':
              C = C + 1
       elif i1 == 'D':
              D = D + 1
       elif i1 == 'F':
              F = F + 1       
       i1 = input().upper()
if i1 == 'Z':
    print("End list")

passing = A + B + C + D

total = passing + F

ppass = float("{0:.2f}".format(((passing / total)) * 100))
pfail = float("{0:.2f}".format((F / total) * 100))
GPA = float("{0:.2f}".format((((A * 4.0) + (B * 3.0) + (C * 2.0) + (D * 1.0)) / total)))

print("Students passing: ", passing, "(",ppass,"%)")
print("Students failing: ", F, "(",pfail,"%)")
print("Class GPA: ", GPA)