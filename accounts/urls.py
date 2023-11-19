from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    UserView,
    ProfileView,
    SubgroupView,
)

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("user/", UserView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("subgroups/", SubgroupView.as_view()),
]
