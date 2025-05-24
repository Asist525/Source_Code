students = [
    ('홍길동', 3.9, 20160303),
    ('김철수', 3.0, 20160302),
    ('최지영', 4.3, 20160301),
 ]
print(sorted(students, key=lambda student: student[1], reverse=True))