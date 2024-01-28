# Represent the information given in student_scores table in appropriate data structure.
# From student_scores data, create a new data structure named best_students_scores, storing the information (name and score) only for students with scores greater than 4.00
# Print out the names and scores from best_students_scores as shown:

student_scores = {
    "Ivan": 5.0,
    "Alex": 3.50,
    "Maria": 5.50,
    "George": 5.00
}

best_students_scores = {k:v for k,v in student_scores.items() if v>4.00}

for k,v in best_students_scores.items():
    print(f'{k:10}- {v}')