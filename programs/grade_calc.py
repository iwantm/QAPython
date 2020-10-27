def avg():
    m = int(input("Please enter your maths mark: "))
    c = int(input("Please enter your chemistry mark: "))
    p = int(input("Please enter your physics mark: "))
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
        grade = 'F'
    return(f'Your percentage score is: {ave}% \nYou scored a grade of: {grade}')
