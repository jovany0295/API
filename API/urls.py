
from django.db import router
from django.urls import path, include
from rest_framework import routers, urlpatterns

from .views import  *
router = routers.DefaultRouter()
router.register(r'Imagenes',ImagenesViewSet)
router.register(r'Videos',VideosViewSet)
router.register(r'Invitado',InvitadoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    
]