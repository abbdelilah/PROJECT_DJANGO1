
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from Rhapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

router = routers.DefaultRouter()
router.register(r'superviseur', views.Superviseur)
router.register(r'personne', views.Personne)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
