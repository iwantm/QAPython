from math import floor


def avg(maths_mark, chem_mark, physics_mark):
    m = maths_mark
    c = chem_mark
    p = physics_mark
    ave = (m+c+p)/3
    if ave >= 70:
        grade = 'A'
    elif ave >= 60:
        grade = 'B'
    elif ave >= 50:
        grade = 'C'
    elif ave >= 40:
        grade = 'D'
    else:
        return('You failed')
    return(f'Your percentage score is: {floor(ave)}% \nYou scored a grade of: {grade}')
