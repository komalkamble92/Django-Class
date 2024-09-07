
'''
Django models relationship :-

1. One-to-one relationship: models.OneToOneField(Student, on_delete=models.CASCADE)
examples : user and user profile


2. One-to-many relationship: models.ForeignKey(Student, on_delete=models.CASCADE)
examples : student and course

3. Many-to-many relationship: models.ManyToManyField(Course, through='StudentCourse')
examples : student and subject
[1,2,3]

4. One-to-many relationship with a custom intermediate model: models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses')
5. Many-to-many relationship with a custom intermediate model: models.ManyToManyField(Course, through='StudentCourse')
6. One-to-many relationship with a custom intermediate model and a custom name for the intermediate model: models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_courses')
7. Many-to-many relationship with a custom intermediate model and a custom name for the intermediate model: models.ManyToManyField(Course, through='StudentCourse', related_name='course_students')
8. One-to-many relationship with a custom name for the foreign key: models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_courses')
9. Many-to-many relationship with a custom name for the foreign key: models.ManyToManyField(Course, through='StudentCourse', related_name='course_students')
'''