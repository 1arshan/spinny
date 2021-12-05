from django.urls import path
from .views import UserCreateAPIView,Logout,BoxAddView,BoxUpdateView,BoxListView
from rest_framework.authtoken import views as rviews

urlpatterns =[
    path("add/user", UserCreateAPIView.as_view(), name='user_add'),
    path('login', rviews.obtain_auth_token),
    path('logout',Logout.as_view()),
    path("add/box", BoxAddView.as_view(), name='user_add_box'),
    path("update/box", BoxUpdateView.as_view(), name='user_box'),
    path("list/box", BoxListView.as_view(), name='user_list_box'),
]
