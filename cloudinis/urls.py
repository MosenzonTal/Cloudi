from django.urls import path
from . import views
from .decorators import org_admin_only, unauthenticated_user
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    PolicyListView,
    PolicyCreateView,
    PolicyDeleteView,
    PolicyUpdateView,
    OrganizationCreateView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('view_policies', views.view_policies, name='view_policies'),
    path('violations', views.violations, name='violations'),
    path('scan', views.scan, name='scan'),
    path('new_policy', org_admin_only(PolicyCreateView.as_view()), name='new_policy'),
    path('policies', PolicyListView.as_view(), name='policies'),
    path('policies/<int:pk>/delete/', org_admin_only(PolicyDeleteView.as_view()), name='delete_policy'),
    path('policies/<int:pk>/update/', org_admin_only(PolicyUpdateView.as_view()), name='update_policy'),
    path('new_organization', OrganizationCreateView.as_view(), name='new_organization'),

    path('login/', unauthenticated_user(LoginView.as_view()), name="login"),
    path('register/', views.register, name="register"),
    path('register_org/', unauthenticated_user(OrganizationCreateView.as_view()), name="register_org"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('profile/', views.profile, name="profile"),
    path('change_password/', views.change_password, name="change_password"),
]
