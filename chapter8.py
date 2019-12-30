print("Chapter 8 Examples")

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)
print(cheeses[0])

numbers = [17, 123]
numbers[1] = 5
print(numbers)

cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses
'Brie' in cheeses

for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers[i])

for x in empty:
    print('This never happens.')

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]
t[:4]
t[3:]
t[:]

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)

t=['a','b','c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t4=['d','c','e','a','b']
t4.sort()
print(t4)

t5=['a','b','c']
x=t5.pop(1)
print(t5)
print(x)
del t5[1]
print(t5)

t6=['a', 'b', 'c']
t6.remove('b')
print(t6)

t7 = ['a', 'b', 'c', 'd', 'e', 'f']
del t7[1:5]
print(t7)

t8 = ['a', 'b', 'c', 'd', 'e', 'f']
del t8[1:5]
print(t8)

nums=[3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)


s = 'spam'
t = list(s)
print(t)

g = 'pining for the fjords'
l = g.split()
print(l)
print(l[2])

cut = 'spam-spam-spam'
delimiter = '-'
cut.split(delimiter)

k = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(k)

def delete_head(letters):
    del letters[0]
letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

def tail(t):
    return t[1:]
letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)
['b', 'c']

print("Chapter8 Exercise")

def chop(lst):
    del lst[0]
    del lst[-1]
def middle(lst):
    new = lst[1:]
    del new[-1]
    return new
my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]
chop_list = chop(my_list)
print(my_list)
print(chop_list)
middle_list = middle(my_list2)
print(my_list2)
print(middle_list)

f=input()
fhand = open(f)
weekdays = ['Sun', 'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat']
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if words[2] in weekdays[:]:
      print(words[2])

g=input('file')
fright = open(g)
count = 0
for line in fright:
    words = line.split()
    # print 'Debug:', words
    if (len(words) > 0) and (words[0] == 'From'):
      print(words[2])


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word= line.rstrip().split()
    for element in word:
        if element in lst:
            continue
        else :
            lst.append(element)
lst.sort()
print(lst)

fn=input('enter:')
fleft = open(fn)
count = 0
for line in fleft:
    words = line.split()
    if len(words) < 3 or words[0] != 'from':
        continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)


my_list=[]
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break
    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()
    my_list.append(input_number)
print('Maximum: ', max(my_list))
print('Minimum: ', min(my_list))