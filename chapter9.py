#examplesChap9

eng2sp=dict()
eng2sp={'one':'uno','two':'dos','three':'tres'}

print(eng2sp)
eng2sp['one']='uno'
'one' in eng2sp
'uno' in eng2sp
print(eng2sp['two'])

word='brontosaurus'
d=dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)

counts={'chuck':1,'annie':42,'jan':100}
print(counts.get('jan',0))
print(counts.get('tim',0))

word='brontosaurus'
d=dict()
for c in word:
    d[c]=d.get(c,0)+1
print(d)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)




#1
count = 0
dictionary_words = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue
        dictionary_words[word] = count
if 'Python' in dictionary_words:
    print('True')
else:
    print('False')

#2
dictionary_days = dict()
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1
        else:
            dictionary_days[words[2]] += 1
print(dictionary_days)

#3
dictionary_addresses = dict()
fnam = input('Enter a file name: ')
try:
    fhan = open(fnam)
except FileNotFoundError:
    print('File cannot be opened:', fnam)
    exit()
for line in fhan:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1
        else:
            dictionary_addresses[words[1]] += 1
print(dictionary_addresses)

#4
dictionary_address = dict()
maximum = 0
maximum_address = ''
fna = input('Enter a file name: ')
try:
    fha = open(fna)
except FileNotFoundError:
    print('File cannot be opened:', fna)
    exit()
for line in fha:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    if words[1] not in dictionary_address:
        dictionary_address[words[1]] = 1
    else:
        dictionary_addresses[words[1]] += 1
for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:
        maximum = dictionary_addresses[address]
        maximum_address = address
print(maximum_address, maximum)

#5
dictionary_domains = dict()
fn = input('Enter a file name: ')
try:
    fh = open(fn)
except FileNotFoundError:
    print('File cannot be opened:', fn)
    exit()
for line in fh:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        atpos = words[1].find('@')
        domain = words[1][atpos+1:]
        if domain not in dictionary_domains:
            dictionary_domains[domain] = 1
        else:
            dictionary_domains[domain] += 1
print(dictionary_domains) 