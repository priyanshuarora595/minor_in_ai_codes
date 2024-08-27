def find_top_student(students_scores):
    # Complete this function
    if not students_scores:
        return []

    # Find the highest score
    # print(students_scores.values())
    max_score = max(students_scores.values())
    print(max_score)

    # Find all students with the highest score
    top_students = [
        name for name, score in students_scores.items() if score == max_score
    ]

    return top_students
