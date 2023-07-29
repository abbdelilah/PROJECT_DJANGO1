from django.contrib.auth.models import User, Group
from Rhapp.models import Superviseur, Personne
from rest_framework import viewsets
from rest_framework import permissions
from Rhapp.serializers import PersonneSerializer, SuperviseurSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class Superviseur(viewsets.ModelViewSet):

    queryset = Superviseur.objects.all()
    serializer_class = SuperviseurSerializer
    permissions_class =[permissions.IsAuthenticated]


class Personne(viewsets.ModelViewSet):

    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    permissions_class =[permissions.IsAuthenticated]



