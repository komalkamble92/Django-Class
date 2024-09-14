'''
python3 manage.py shell
>>> shell

from django.contrib.auth.models import User
from appname.models import *
from appname.models import Student
from appname.models import Student, Modelname2, Modelname3,



In [4]: Student.objects.all()
Out[4]: <QuerySet [<Student: AAKANKSHA BAISHWADE>, <Student: Demo_customer Guardians>]>

In [2]: Student.objects.all().values()
Out[2]: <QuerySet [{'id': 1, 'first_name': 'AAKANKSHA', 'last_name': 'BAISHWADE', 'age': 24, 'date_of_birth': datetime.date(2024, 9, 11)}, {'id': 2, 'first_name': 'Demo_customer', 'last_name': 'Guardians', 'age': 20, 'date_of_birth': datetime.date(2023, 10, 18)}]>


In [5]: Student.objects.all().count()
Out[5]: 2


1st way to store data in student table
In [8]: from datetime import date

In [9]: student = Student(first_name='Student', last_name='Student', age=30, date_of_birth = date(2024, 9, 11))

In [10]: student.save()

2ed way to store data in student table

      student = Student.objects.create(
          first_name="Jane",
          last_name="Smith",
          age=22,
          date_of_birth=date(2002, 5, 30)
      )
'''