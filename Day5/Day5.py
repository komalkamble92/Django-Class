'''

5. Field Types:
   - Django provides various field types that correspond to different data types in the database.
   - Common field types include CharField, IntegerField, BooleanField, DateField, DateTimeField, 
   ForeignKey, ManyToManyField, etc.
   - https://docs.djangoproject.com/en/5.0/ref/models/fields/

6. Example:
   - Here's an example of creating a simple Django model for a Student table with a few fields:
     from django.db import models

     class Student(models.Model):
         first_name = models.CharField(max_length=100)
         last_name = models.CharField(max_length=100)
         age = models.IntegerField()
         date_of_birth = models.DateField()
         
7. Interacting with Databases:

* Interacting with databases in Django can be done in two main ways: the "dumb way" and the "MTV way"
 (Model-Template-View way).

* The "dumb way" refers to directly writing SQL queries in your views or other parts of your
 code to interact with the database. This approach is discouraged in Django as it bypasses Django's
   ORM and can lead to low security and code that is difficult to maintain.
* The "MTV way" involves using Django's ORM (Object-Relational Mapping) to interact with the database. 
This approach is recommended as it abstracts away the details of the database and allows you to work with 
Python objects instead of raw SQL.

'''

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
