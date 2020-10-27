file = open('teams.txt', 'r')
lines = file.readlines()

file = open('teams.txt', 'w')

file.write('This is a new line \n')
for line in lines:
    file.write(line)

file = open('teams.txt', 'r')
lines = file.readlines()
file.seek(0)
for line in range(len(lines)):
    print(file.readline())
file.close()
