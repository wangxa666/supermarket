from django.test import TestCase

# Create your tests here.


import re


a = 'Abc'

b = 'abc'


c = re.match(a,b,re.IGNORECASE)

print(c)
