from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('assets', views.AssetsView)
router.register('liabilities', views.LiabilitiesView)
router.register('expenses', views.ExpensesView)
router.register('get_user_data', views.GetAllUserInfo, basename='get_user_data')

urlpatterns = [
    path('', include(router.urls)),
]
