'''
getting all data 

1. Student.objects.all()
2. Student.objects.filter(student_name='ram').
2. Student.objects.create(name='Student', age=4)
2. Student.objects.exclude(student_name='ram')
3. Student.objects.get(student_name='ram')
4. Student.objects.order_by('student_name')
5. Student.objects.filter(student_name='ram').order_by('student_name')
6. Student.objects.values('student_name')
7. Student.objects.values_list('student_name')
8. Student.objects.annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).filter(age_diff__gt=10)
9. Student.objects.annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).order_by('-age_diff')
10. Student.objects.annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).values('student_name', 'age_diff')
11. Student.objects.annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).values_list('student_name', 'age_diff')
'''