from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('langauges', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('programmers', views.ProgrammerView)
router.register('register', views.RegisterView, 'users-register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='users-login')
]
