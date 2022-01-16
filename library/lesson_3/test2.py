from rest_framework import serializers
#from test1 import Author

#
# class AuthorSerializer(serializers.Serializer):
#    name = serializers.CharField(max_length=128)
#    birthday_year = serializers.IntegerField()
#
#    def create(self, validated_data):
#        return Author(**validated_data)
#
#    def update(self, instance, validated_data):
#        instance.name = validated_data.get('name', instance.name)
#        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
#        return instance
#
#
# data = {'name': 'Грин', 'birthday_year': 1880}
# serializer = AuthorSerializer(data=data)
# serializer.is_valid()
# author = serializer.save()
# print(author.name, author.birthday_year)
#
# data = {'name': 'Александр', 'birthday_year': 1880}
# serializer = AuthorSerializer(author, data=data)
# serializer.is_valid()
# author = serializer.save()
# print(author.name, author.birthday_year)
#
# data = {'birthday_year': 2000}
# serializer = AuthorSerializer(author, data=data, partial=True)
# serializer.is_valid()
# author = serializer.save()
# print(author.name, author.birthday_year)





#
# class AuthorSerializer(serializers.Serializer):
#    name = serializers.CharField(max_length=128)
#    birthday_year = serializers.IntegerField()
#
# data = {'name': 'Грин', 'birthday_year': 1880}
# serializer = AuthorSerializer(data=data)
# print(serializer.is_valid())  # True
#
# data = {'name': 'Грин', 'birthday_year': 'abc'}
# serializer = AuthorSerializer(data=data)
# print(serializer.is_valid())  # False
#
# print(serializer.errors)  # {'birthday_year': [ErrorDetail(string='A valid integer is required.', code='invalid')]}
#
# serializer.is_valid(raise_exception=True)





# class AuthorSerializer(serializers.Serializer):
#    name = serializers.CharField(max_length=128)
#    birthday_year = serializers.IntegerField()
#
#    def validate_birthday_year(self, value):
#        if value < 0:
#            raise serializers.ValidationError('Год рождения не может быть отрицательным')
#        return value
#
#    def validate(self, attrs):
#        if attrs['name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
#            raise serializers.ValidationError('Неверный год рождения Пушкина')
#        return attrs
#
# data = {'name': 'Грин', 'birthday_year': 1880}
# serializer = AuthorSerializer(data=data)
# print(serializer.is_valid())  # True
#
# data = {'name': 'Пушкин', 'birthday_year': 1880}
# serializer = AuthorSerializer(data=data)
# print(serializer.is_valid())  # True
