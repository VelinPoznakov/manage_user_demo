from django.urls import path

from manae_users_demos.auth_app.views import HomePage, RegisterUserView, LoginViewTemplate, LogoutViewTemplate, \
    UserToDoList, ToDoCreateView, ToDoDelete, MyAccount

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginViewTemplate.as_view(), name='login'),
    path('logout/', LogoutViewTemplate.as_view(), name='logout'),
    path('to_do/', UserToDoList.as_view(), name='to_do'),
    path('to_do_create/', ToDoCreateView.as_view(), name='to_do_create'),
    path('to_do/<int:pk>/', ToDoDelete.as_view(), name='delete'),
    path('account/<int:pk>/', MyAccount.as_view(), name='account'),

]
