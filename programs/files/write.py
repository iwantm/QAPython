teams = ['Burnley FC ', 'Accrington Stanley',
         'Colne FC', 'Nelson FC', 'AFC Burnley']

file = open('teams.txt', "w")

for team in teams:
    line = team + '\n'
    file.write(line)

file = open('teams.txt', 'r')

print(file.readline())
file.readline()
file.readline()
print(file.readline())
file.close()
