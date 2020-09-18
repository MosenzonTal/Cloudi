from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('ActivatedPolicy', views.ActivatedPolicyView)
router.register('Violation', views.ViolationView)


urlpatterns = [
    path('', include(router.urls)),
]
