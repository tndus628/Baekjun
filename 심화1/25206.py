credit=0
total = 0
# for i in range(20):
#     a,b,c = input().split()
#     b = float(b)
   
#     if c=="A+":
#         total += b*4.5
#     elif c=="A0":
#         total += b*4.0
#     elif c=="B+":
#         total += b*3.5
#     elif c=="B0":
#         total += b*3.0
#     elif c=="C+":
#         total += b*2.5
#     elif c=="C0":
#         total += b*2.0
#     elif c=="D+":
#         total += b*1.5
#     elif c=="D0":
#         total += b*1.0
#     elif c=="F":
#         total += b*0.0
#     else:
#         continue
#     credit += b

# print(total/credit)

grade = { "A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0 }

for i in range(20):
    a, b, c = input().split()
    b = float(b)
    # print(grade[c])
    if c=="P":
        continue
    total += grade[c] * b
    credit += b
print(total/credit)




