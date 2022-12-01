from django.urls import path

from applications.account.views import *


urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('change_password/', Change_passwordApiView.as_view()),
    path('send_mail/', send_hello_api_view)
]


