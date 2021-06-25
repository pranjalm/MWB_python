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

'''
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
'''


'''
# correct indent is like this
# you need to go back to same indent for elif part.
# elif/else part should be directly below if part.
marks = int(input())
if(marks<100 and marks>=90):
    print("A division")
elif(marks<90 and marks>=80):
    print("B division")
elif(marks<80 and marks>=60):
    print("C division")
elif(marks<60 and marks>=40):
    print("D division")
else:
    print("fail")
'''


# if a = 10 then print 1 to 10 (inclusive)
#a = int(input())
'''
for i in range(1,a+1):
    print(i)

i = 1
while(i<=10):    
    print(i)
    i = i+1
'''

# prime number -> yes or no
# 1. take number input.
# 2. check primeness.
#   a.
#   b.
# 3. print(yes or no)


a = int(input())

def is_prime(a):
    return_type = True
    for i in range(2,a):
        if(a%i==0):
            return_type = False
            break
        else:
            return_type = True
    return return_type


if(a==1 or a==2 or a==3):
    print("prime number")
elif(is_prime(a)==True):
    print("prime number")
else:
    print("not prime number")


'''
def addtn(a,b):
    return a+b
sum1 = addtn(int(input()),int(input()))
print(sum1)
'''

# homework (25 June 2021)
'''
Make the prime number program more syntectically small.
2. Type fibbonaci sequance till given input.
'''



























