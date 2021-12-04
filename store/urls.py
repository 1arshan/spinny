from django.urls import path
from .views import UserCreateAPIView,Logout,BoxView
from rest_framework.authtoken import views as rviews

urlpatterns =[
    path("add/user", UserCreateAPIView.as_view(), name='user_add'),
    path('login', rviews.obtain_auth_token),
    path('logout',Logout.as_view()),
    path("add/box", BoxView.as_view(), name='user_box'),
]
