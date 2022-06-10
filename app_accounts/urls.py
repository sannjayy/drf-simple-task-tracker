from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import LoginAPIView, UserAccountView, LogoutAPIView, LogoutAllView

app_name = 'accounts'

urlpatterns = [
    path('account/', UserAccountView.as_view(), name="account"),

    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name="verify_token"),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('auth/logout/', LogoutAPIView.as_view(), name='logout'),
    path('auth/logout/all/', LogoutAllView.as_view(), name='logout_all'),   
]