student_scores = {
    'ivan':4.5,
    'maria':5.0,
    'asen':3.5
}

best_students = {k:v for k,v in student_scores.items() if v>4}

print(best_students)