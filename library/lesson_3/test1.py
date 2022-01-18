class Author:

   def __init__(self, name, birthday_year):
       self.name = name
       self.birthday_year = birthday_year

   def __str__(self):
       return self.name


class Biography:

   def __init__(self, text, author):
       self.author = author
       self.text = text


class Book:

   def __init__(self, name, authors):
       self.name = name
       self.authors = authors


class Article:

   def __init__(self, name, author):
       self.name = name
       self.author = author

from rest_framework import serializers

class AuthorSerializer(serializers.Serializer):
   name = serializers.CharField(max_length=128)
   birthday_year = serializers.IntegerField()

author = Author('Грин', 1880)
serializer = AuthorSerializer(author)
print(serializer.data)  # {'name': 'Грин', 'birthday_year': 1880}
print(type(serializer.data))  # <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo")
from rest_framework.renderers import JSONRenderer
renderer = JSONRenderer()
json_bytes = renderer.render(serializer.data)
print(json_bytes)  # b'{"name":"\xd0\x93\xd1\x80\xd0\xb8\xd0\xbd","birthday_year":1880}'
print(type(json_bytes))  # <class 'bytes'>

import io
from rest_framework.parsers import JSONParser
stream = io.BytesIO(json_bytes)
data = JSONParser().parse(stream)
print(data)  # {'name': 'Грин', 'birthday_year': 1880}
print(type(data))  # <class 'dict'>

serializer = AuthorSerializer(data=data)
print(serializer.is_valid())  # True
print(serializer.validated_data)  # OrderedDict([('name', 'Грин'), ('birthday_year', 1880)])
print(type(serializer.validated_data))  # <class 'collections.OrderedDict'>