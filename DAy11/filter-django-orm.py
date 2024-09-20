'''

-------------filter-------------------

Student.objects.filter(age__lt=25)

filter = Student.objects.filter(field_name)

field_name=value (Exact match)
field_name__icontains=value (Case-insensitive containment test)
field_name__gte=value (Greater than or equal to)
field_name__lte=value (Less than or equal to)
field_name__startswith=value (Starts with)
field_name__endswith=value (Ends with)
field_name__in=[value1, value2] (Contained within a list)
field_name__isnull=True (Is null)
'''