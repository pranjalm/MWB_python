'''
a = input()
b = input()
c = input()
x = int(a)
y = int(b)
z = int(c)
print(x+y+z)
print(x*y*z)
print(x/z)
print(x-y)
'''


# github profile upload
# session-2
# if else statement

Marks = int(input())

# if 1st number is bigger -> print("first") otherwise -> print("second")
# Grading  categories mark = 0-100;
# A div = 60(inclusive)-100(inclusive)
# B div = 40(inclusive)-60
# C div = 30(inclusive)-40
# Fail = 0 - 30

if(Marks<=100 and Marks>=60):
    print("A division")
elif(Marks<60 and Marks>=40):
    print("B division")
elif(Marks<40 and Marks>=30):
    print("C division")
else:
    print("Fail")
    
