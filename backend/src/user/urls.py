from django.conf.urls import url
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserRegistrationView, UserLoginView, UserView

urlpatterns = [
    # path('current_user/', current_user),
    # path('users/', UserList.as_view()),
    # path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^register', UserRegistrationView.as_view()),
    url(r'^login', UserLoginView.as_view()),
    url(r'^current_user', UserView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
