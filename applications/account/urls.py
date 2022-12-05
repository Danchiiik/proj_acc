from django.urls import path

from applications.account.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    # path('login/', LoginApiView.as_view()),
    # path('logout/', LogoutApiView.as_view()),
    path('change_password/', Change_passwordApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('send_mail/', send_hello_api_view),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view())
    
]


