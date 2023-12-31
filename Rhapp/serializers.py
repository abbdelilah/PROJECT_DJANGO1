from django.contrib.auth.models import User, Group
from Rhapp.models import Superviseur, Personne
from Rhapp.models import User




from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SuperviseurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Superviseur
        fields = ['nom', 'Prenom', 'departement', 'active', 'user']


class PersonneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personne
        fields = ['nom', 'Prenom', 'departement', 'active', 'user', 'Superviseur', 'date_of_formation']


        