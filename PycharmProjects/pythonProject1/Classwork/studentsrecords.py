def student_rec():
    # student1 = {'id': 1, 'name': "Segun", 'scores': (10, 20, 30)}
    # student2 = {'id': 2, 'name': "Retna", 'scores': (12, 22, 32)}
    # student3 = {'id': 3, 'name': "Ebuka", 'scores': (14, 24, 34)}
    #
    # studentrec = []
    # studentrec = student1 + student2 + student3
    # print(studentrec)

    student_records = [
        {'id': 1, 'name': "Segun", 'scores': (10, 20, 30)},
        {'id': 2, 'name': "Retna", 'scores': (12, 22, 32)},
        {'id': 3, 'name': "Ebuka", 'scores': (14, 24, 34)},
    ],
    student_records.append({'id': 4, 'name': "Jibola", 'scores': (34, 44, 54)})
    print(student_records)

    student_records.pop(3)
    print(student_records)


student_rec()
