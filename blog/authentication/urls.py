from django.urls import path
from authentication.views import MyObtainTokenPairView, RegisterView, ChangePasswordView, LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout-all/', LogoutAllView.as_view(), name='auth_logout_all'),
]