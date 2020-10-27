def grade(Name, Homework, Assessment, Exam):
    grades = Homework/25 + Assessment/50 + Exam/100
    avg_grade = grades/3 * 100
    letter = ''
    if avg_grade >= 70:
        letter = 'A'
    elif avg_grade >= 60:
        lettter = 'B'
    elif avg_grade >= 50:
        letter = 'C'
    elif avg_grade >= 40:
        letter = 'D'
    else:
        return(f'{Name} Failed. Final Grade: {avg_grade}%')
    return(f'{Name} achieved {avg_grade}%. Final grade: {letter}')
