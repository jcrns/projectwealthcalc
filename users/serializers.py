from rest_framework import serializers
from .models import Language, Paradigm, Programmer
from django.contrib.auth.models import User

class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')

class ParadigmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')

class ProgrammerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')