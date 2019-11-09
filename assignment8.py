x=3
if x<10:
    print("Small")

x=4
if x%2==0:
    print("x is even")
else:
    print("x is odd")


x=3
y=5
if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print ("x is equal to y")


x=6
y=3
if x==y:
    print("x and y are equal")
else:
    if x<y:
        print("x is less than y")
    else:
        print("x is greater than y")


inp=input("Enter Fahrenheit Temperature:")
fahr=float(inp)
cel=(fahr-32.0)*5.0/9.0
print(cel)



inp=input("Enter Fahrenheit Temperature:")
try:
    fahr=float(inp)
    cel=(fahr-32.0)*5.0/9.0
    print(cel)
except:
    print("Please enter a number.")



input_hours=input("Enter Hours: ")
input_rate=input("Enter Rate: ")
hours=float(input_hours)
rate=float(input_rate)
if hours<40:
    pay=rate*hours
else:
    overtime=hours-40
    pay=(rate*40.0)+(1.5*rate*overtime)
print("Pay: ",pay)



input_hours=input("Enter Hours: ")
try:
    hours=float(input_hours)
except:
    print("Error, please enter a numeric input!")
input_rate=input("Enter Rate: ")
try:
    rate=float(input_rate)
except:
    print("Error, please enter a numeric input!")
if hours<40:
    pay=rate*hours
else:
    overtime=hours-40
    pay=(rate*40.0)+(1.5*rate*overtime)
print("Pay:", pay)


score=0.0
grade=""
input1=input("Enter score ")
try:
    score=float(input1)
except:
    print("Bad Score")
    quit()
if 0.0<=score<=1.0:
    if score>=0.9:
        grade="A"
    elif score>=0.8:
        grade="B"
    elif score>=0.7:
        grade="C"
    elif score>=0.6:
        grade="D"
    else:
        grade="F"
else:
    grade="Bad Score"
print(grade)





import random
for i in range(10):
    x = random.random()
    print(x)


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print_lyrics()
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()


def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice('Spam')
print_twice(17)
print_twice('Spam '*4)


michael = 'Eric, the half a bee.'
print_twice(michael)


result = print_twice('Bing')


def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)



def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()



def computepay(tmp_hours, tmp_rate):
    if tmp_hours <= 40.0:
        return tmp_rate * tmp_hours
    overtime = tmp_hours - 40.0
    return (tmp_rate * 40.0) + (1.5 * tmp_rate * overtime)
def check_for_float(input1):
    try:
        val = float(input1)
        return val
    except:
        print('Error, please enter numeric input')
        quit()
input_hours = input('Enter Hours: ')
hours = check_for_float(input_hours)
input_rate = input('Enter Rate: ')
rate = check_for_float(input_rate)
pay = computepay(hours, rate)
print('Pay: ', pay)


def computegrade(tmp_score):
    if 0.0 <= tmp_score <= 1.0:
        if tmp_score >= 0.9:
            return 'A'
        if tmp_score >= 0.8:
            return 'B'
        if tmp_score >= 0.7:
            return 'C'
        if tmp_score >= 0.6:
            return 'D'
        return 'F'
    return 'Bad score'
input_score = input('Enter score: ')
score = 0.0
try:
    score = float(input_score)
except:
    print('Bad score')
    quit()
grade = computegrade(score)
print(grade)

