from django.urls import path
from users.apps import UsersConfig

# from rest_framework.permissions import AllowAny


# from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    # path('register/', UserCreateAPIView.as_view(), name='register'),
    # path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
