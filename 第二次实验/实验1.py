import random

students = {'学号{:04d}'.format(i + 201800): {'语文': random.randint(50, 150), '数学': random.randint(50, 150), '英语': random.randint(50, 150)} for i in range(40)}
for student, scores in students.items():
    scores['总分'] = sum(scores.values())
sorted_students = sorted(students.items(), key=lambda x: x[1]['总分'], reverse=True)
for student, scores in sorted_students:
    print(f"{student}: 总分 {scores['总分']}")
