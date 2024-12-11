courses = [99,98,30,20,100]
total = 0

for n in range( len(courses)-1 ):
    total += courses[n]
else:
    print(total)

for n in courses[ 0:3 ]:
    total += n
else:
    print(total)